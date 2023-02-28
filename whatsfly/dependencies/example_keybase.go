package keybase

import (
	"encoding/json"
	"errors"
	"fmt"
	"strings"
)

const (
	mnemonicEntropySize = 256
	defaultCoinType     = 688
)

var gCdc = codec.New()
var _ KeyBase = DefaultKeyBase{}

type KeyBase interface {
	CreateKey(name, password, bip39Passphrase string, account, index uint32) string
	DeleteKey(name, password string) string
}

type DefaultKeyBase struct {
	kb   keys.Keybase
	name string
	dir  string
}

func NewDefaultKeyBase(root string) DefaultKeyBase {
	initDefaultKeyBaseConfig()
	return DefaultKeyBase{
		keys.New("keys", root),
		"keys",
		root,
	}
}

// todo: name repetition check
func (k DefaultKeyBase) CreateKey(name, password, bip39Passphrase string, account, index uint32) string {
	exist := k.GetAddress(name)
	if !strings.HasPrefix(exist, errPrefix) {
		return createKeyErr(errors.New("key with same name is already exist"))
	}
	if l := len(password); l < 8 {
		s := fmt.Sprintf("password len %d is too short", l)
		return createKeyErr(errors.New(s))
	}

	entropySeed, err := bip39.NewEntropy(mnemonicEntropySize)
	if err != nil {
		return createKeyErr(err)
	}

	mnemonic, err := bip39.NewMnemonic(entropySeed[:])
	if err != nil {
		return createKeyErr(err)
	}
	hdPath := hd.NewFundraiserParams(account, defaultCoinType, index)
	info, err := k.kb.Derive(name, mnemonic, bip39Passphrase, password, *hdPath)
	if err != nil {
		return createKeyErr(err)
	}
	return info.GetAddress().String() + "+" + mnemonic
}

func (k DefaultKeyBase) DeleteKey(name, password string) string {
	if err := k.kb.Delete(name, password, false); err != nil {
		return deleteKeyErr(err)
	}
	return ""
}

func initDefaultKeyBaseConfig() {
	initCodec()
	bench32MainPrefix := "coinex"
	bench32PrefixAccAddr := bench32MainPrefix
	// bench32PrefixAccPub defines the bench32 prefix of an account's public key
	bench32PrefixAccPub := bench32MainPrefix + sdk.PrefixPublic
	// bench32PrefixValAddr defines the bench32 prefix of a validator's operator address
	bench32PrefixValAddr := bench32MainPrefix + sdk.PrefixValidator + sdk.PrefixOperator
	// bench32PrefixValPub defines the bench32 prefix of a validator's operator public key
	bench32PrefixValPub := bench32MainPrefix + sdk.PrefixValidator + sdk.PrefixOperator + sdk.PrefixPublic
	// bench32PrefixConsAddr defines the bench32 prefix of a consensus node address
	bench32PrefixConsAddr := bench32MainPrefix + sdk.PrefixValidator + sdk.PrefixConsensus
	// bench32PrefixConsPub defines the bench32 prefix of a consensus node public key
	bench32PrefixConsPub := bench32MainPrefix + sdk.PrefixValidator + sdk.PrefixConsensus + sdk.PrefixPublic

	config := sdk.GetConfig()
	config.SetCoinType(defaultCoinType)
	config.SetBech32PrefixForAccount(bench32PrefixAccAddr, bench32PrefixAccPub)
	config.SetBech32PrefixForValidator(bench32PrefixValAddr, bench32PrefixValPub)
	config.SetBech32PrefixForConsensusNode(bench32PrefixConsAddr, bench32PrefixConsPub)
	config.Seal()
}

func initCodec() {
	gCdc.RegisterInterface((*crypto.PubKey)(nil), nil)
	gCdc.RegisterInterface((*crypto.PrivKey)(nil), nil)
	gCdc.RegisterInterface((*sdk.Msg)(nil), nil)
	gCdc.RegisterConcrete(secp256k1.PubKeySecp256k1{}, "tendermint/PubKeySecp256k1", nil)
	gCdc.RegisterConcrete(secp256k1.PrivKeySecp256k1{}, "tendermint/PrivKeySecp256k1", nil)
}

func GetAddressFromEntropy(entropy []byte) (string, string, error) {
	mnemonic, err := bip39.NewMnemonic(entropy)
	if err != nil {
		return "", mnemonic, err
	}

	DefaultBIP39Passphrase := ""
	seed := bip39.NewSeed(mnemonic, DefaultBIP39Passphrase)
	fullHdPath := hd.NewFundraiserParams(0, defaultCoinType, 0) //account=0 addressIdx=0
	masterPriv, ch := hd.ComputeMastersFromSeed(seed)
	derivedPriv, err := hd.DerivePrivateKeyForPath(masterPriv, ch, fullHdPath.String())
	pubk := secp256k1.PrivKeySecp256k1(derivedPriv).PubKey()
	addr := pubk.Address()
	acc := sdk.AccAddress(addr)
	return acc.String(), mnemonic, nil
}

func infosToJson(infos []keys.Info) (string, error) {
	kos, err := keys.Bech32KeysOutput(infos)
	if err != nil {
		return "", err
	}
	out, err := json.Marshal(kos)
	if err != nil {
		return "", err
	}
	return string(out), nil
}

func NewWIF() {

}
