package main
// #include "wapp.h"
import "C"

import (
	"os"
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
    "google.golang.org/protobuf/proto"
    _ "modernc.org/sqlite"
    // sqlite3 "github.com/mattn/go-sqlite3"

)

var WpClient *whatsmeow.Client

//export Connect
func Connect() {

	// Set the path for the database file
    dbPath := "database/wapp.db"

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

//export SendMessage
func SendMessage(number *C.char, msg *C.char) C.int {
    jid := types.JID{
        User:   C.GoString(number),
        Server: types.DefaultUserServer,
    }
    message := &waProto.Message{
        Conversation: proto.String(C.GoString(msg)),
    }

    // Check if the client is connected
    fmt.Println("Check WpConnetion")
    if !WpClient.IsConnected() {
    	fmt.Println("WpCLient NotCnnected")
        err := WpClient.Connect()
        if err != nil {
            return 1
        }
    }
    fmt.Println("WpConneted")	
    
    _, err := WpClient.SendMessage(context.Background(), jid, message)
    if err != nil {
        return 1
    }
    return 0
}

func main() {
    // // Listen to Ctrl+C (you can also do something else that prevents the program from exiting)
    // c := make(chan os.Signal)
    // signal.Notify(c, os.Interrupt, syscall.SIGINT, syscall.SIGTERM)
    // <-c

    // client.Disconnect()

}
