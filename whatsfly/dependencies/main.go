package main
// #include "wapp.h"
import "C"

import (
	"os"
    "net/http"
    // "os/signal"
    // "syscall"
	"path/filepath"
	"fmt"
    "context"
    "github.com/mdp/qrterminal/v3"
    "go.mau.fi/whatsmeow"
    waProto "go.mau.fi/whatsmeow/binary/proto"
    "go.mau.fi/whatsmeow/store/sqlstore"
    "go.mau.fi/whatsmeow/types"
    waLog "go.mau.fi/whatsmeow/util/log"
    "go.mau.fi/whatsmeow/store"
    "google.golang.org/protobuf/proto"
    _ "modernc.org/sqlite"
    // sqlite3 "github.com/mattn/go-sqlite3"

)

var WpClient *whatsmeow.Client

//export Connect
func Connect() {
	// Set the path for the database file
    dbPath := "database/wapp.db"

    // Set Browser
    store.DeviceProps.PlatformType = waProto.DeviceProps_SAFARI.Enum()
    store.DeviceProps.Os = proto.String("macOS") //"Mac OS 10"

    // Create the directory if it doesn't exist
    err := os.MkdirAll(filepath.Dir(dbPath), 0755)
    if err != nil {
        panic(err)
    }

    // Connect to the database
    container, err := sqlstore.New("sqlite", "file:"+dbPath+"?_foreign_keys=on", waLog.Noop)
    if err != nil {
        panic(err)
    }

    deviceStore, err := container.GetFirstDevice()
    if err != nil {
        panic(err)
    }
    client := whatsmeow.NewClient(deviceStore, waLog.Noop)

    if client.Store.ID == nil {
        // No ID stored, new login
        qrChan, _ := client.GetQRChannel(context.Background())
        err = client.Connect()
        if err != nil {
            panic(err)
        }
        for evt := range qrChan {
            if evt.Event == "code" {
                qrterminal.GenerateHalfBlock(evt.Code, qrterminal.L, os.Stdout)
            } else {
                fmt.Println("Login event:", evt.Event)
            }
        }
    } else {
        err := client.Connect()
        fmt.Println("User already logged in")
        if err != nil {
            panic(err)
        }
    }

    WpClient = client		
}

func assignUserJid(number string) types.JID {
    jid := types.JID{
        User:   number,
        Server: types.DefaultUserServer,
    }
    return jid
}

func assignGroupJid(number string) types.JID {
    jid := types.JID{
        User:   number,
        Server: types.GroupServer,
    }
    return jid
}

func _SendMessage(number types.JID, msg *C.char) C.int {
    // safely reset the msg string. there is a concat issue
    message := &waProto.Message{
        Conversation: proto.String(""),
    }
    message.Conversation = proto.String(C.GoString(msg))

    // Check if the client is connected
    if !WpClient.IsConnected() {
        err := WpClient.Connect()
        if err != nil {
            return 1
        }
    }
    
    _, err := WpClient.SendMessage(context.Background(), number, message)
    if err != nil {
        return 1
    }
    return 0
}

//export SendMessage
func SendMessage(number *C.char, msg *C.char) C.int {
    var jid types.JID = assignUserJid(C.GoString(number))
    return _SendMessage(jid, msg)
}

//export SendGroupMessage
func SendGroupMessage(number *C.char, msg *C.char) C.int {
    var jid types.JID = assignGroupJid(C.GoString(number))
    return _SendMessage(jid, msg)
}

func _SendImage(number types.JID, imagePath *C.char, caption *C.char) C.int {

    // type imageStruct struct {
    //     Phone       string
    //     Image       string
    //     Caption     string
    //     Id          string
    //     ContextInfo waProto.ContextInfo
    // }
        // Check if the client is connected
    if !WpClient.IsConnected() {
        err := WpClient.Connect()
        if err != nil {
            return 1
        }
    }

    // var filedata []byte
    filedata, err := os.ReadFile(C.GoString(imagePath))
    if err != nil {
        return 1
    }
    
    var uploaded whatsmeow.UploadResponse
    uploaded, err = WpClient.Upload(context.Background(), filedata, whatsmeow.MediaImage)
    if err != nil {
        return 1
    }
    // "data:image/png;base64,\""

    msg := &waProto.Message{ImageMessage: &waProto.ImageMessage{
        Caption:       proto.String(C.GoString(caption)),
        Url:           proto.String(uploaded.URL),
        DirectPath:    proto.String(uploaded.DirectPath),
        MediaKey:      uploaded.MediaKey,
        Mimetype:      proto.String(http.DetectContentType(filedata)),
        FileEncSha256: uploaded.FileEncSHA256,
        FileSha256:    uploaded.FileSHA256,
        FileLength:    proto.Uint64(uint64(len(filedata))),
    }}
    _, err = WpClient.SendMessage(context.Background(), number, msg)
    if err != nil {
        return 1
    }
    return 0
}

//export SendImage
func SendImage(number *C.char, imagePath *C.char, caption *C.char) C.int {
    var jid types.JID = assignUserJid(C.GoString(number))
    return _SendImage(jid, imagePath, caption)
}

//export SendGroupImage
func SendGroupImage(number *C.char, imagePath *C.char, caption *C.char) C.int {
    var jid types.JID = assignGroupJid(C.GoString(number))
    return _SendImage(jid, imagePath, caption)
}

func main() {
}
