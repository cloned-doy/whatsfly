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