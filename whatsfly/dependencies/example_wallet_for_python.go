package main

/*
 */
import "C"

import (
	"github.com/coinexchain/polarbear/keybase"
)

var ApiForPython WalletForPython

type WalletForPython struct {
	keybase.KeyBase
}

//export BearInit
func BearInit(root *C.char) {
	ApiForPython.KeyBase = keybase.NewDefaultKeyBase(C.GoString(root))
}

//export CreateKey
func CreateKey(name, password, bip39Passphrase *C.char, account, index C.uint) *C.char {
	res := ApiForPython.CreateKey(C.GoString(name), C.GoString(password), C.GoString(bip39Passphrase), uint32(account), uint32(index))
	return C.CString(res)
}

//export DeleteKey
func DeleteKey(name, password *C.char) *C.char {
	return C.CString(ApiForPython.DeleteKey(C.GoString(name), C.GoString(password)))
}

//export RecoverKey
func RecoverKey(name, mnemonic, password, bip39Passphrase *C.char, account, index C.uint) *C.char {
	return C.CString(ApiForPython.RecoverKey(C.GoString(name), C.GoString(mnemonic), C.GoString(password), C.GoString(bip39Passphrase), uint32(account), uint32(index)))
}

//export AddKey
func AddKey(name, armor, passphrase *C.char) *C.char {
	return C.CString(ApiForPython.AddKey(C.GoString(name), C.GoString(armor), C.GoString(passphrase)))
}

//export ExportKey
func ExportKey(name, decryptPassphrase, encryptPassphrase *C.char) *C.char {
	return C.CString(ApiForPython.ExportKey(C.GoString(name), C.GoString(decryptPassphrase), C.GoString(encryptPassphrase)))
}

//export ListKeys
func ListKeys() *C.char {
	return C.CString(ApiForPython.ListKeys())
}

//export ResetPassword
func ResetPassword(name, password, newPassword *C.char) *C.char {
	return C.CString(ApiForPython.ResetPassword(C.GoString(name), C.GoString(password), C.GoString(newPassword)))
}

//export GetAddress
func GetAddress(name *C.char) *C.char {
	return C.CString(ApiForPython.GetAddress(C.GoString(name)))
}

//export GetSigner
func GetSigner(signInfo *C.char) *C.char {
	return C.CString(ApiForPython.GetSigner(C.GoString(signInfo)))
}

//export GetPubKey
func GetPubKey(name *C.char) *C.char {
	return C.CString(ApiForPython.GetPubKey(C.GoString(name)))
}

//export GetAddressFromWIF
func GetAddressFromWIF(wif *C.char) *C.char {
	return C.CString(ApiForPython.GetAddressFromWIF(C.GoString(wif)))
}

//export Sign
func Sign(name, password, tx *C.char) *C.char {
	return C.CString(ApiForPython.Sign(C.GoString(name), C.GoString(password), C.GoString(tx)))
}

//export SignStdTx
func SignStdTx(name, password, tx, chainId *C.char, accountNum, sequence C.ulonglong) *C.char {
	return C.CString(ApiForPython.SignStdTx(C.GoString(name), C.GoString(password), C.GoString(tx), C.GoString(chainId), uint64(accountNum), uint64(sequence)))
}

//export SignAndBuildBroadcast
func SignAndBuildBroadcast(name, password, tx, chainId, mode *C.char, accountNum, sequence C.ulonglong) *C.char {
	return C.CString(ApiForPython.SignAndBuildBroadcast(C.GoString(name), C.GoString(password), C.GoString(tx), C.GoString(chainId), C.GoString(mode), uint64(accountNum), uint64(sequence)))
}

func main() {

}
