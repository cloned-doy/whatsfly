#!/bin/sh

# This build.sh file was borrowed from https://github.com/bogdanfinn/tls-client/blob/master/cffi_whatsmeow/build.sh
# make sure you have installed all build tools on your machine

# echo 'Build OSX'
# GOOS=darwin GOARCH=arm64 go build -o ./whatsmeow/whatsmeow-darwin-arm64.dylib -buildmode=c-shared main.go
# GOOS=darwin GOARCH=amd64 go build -buildmode=c-shared -o ./whatsmeow/whatsmeow-darwin-amd64.dylib main.go

echo 'Build for Windows 32 Bit'
GOOS=windows GOARCH=386 CGO_ENABLED=1 CC=i686-w64-mingw32-gcc go build -buildmode=c-shared -o ./whatsmeow/whatsmeow-windows-32.dll main.go

echo 'Build for Windows amd64 Bit'
GOOS=windows GOARCH=amd64 CGO_ENABLED=1 CC=x86_64-w64-mingw32-gcc go build -buildmode=c-shared -o ./whatsmeow/whatsmeow-windows-64.dll main.go

echo 'Build for Linux Ubuntu'
GOOS=linux GOARCH=amd64 CGO_ENABLED=1 go build -buildmode=c-shared -ldflags=-s -o ./whatsmeow/whatsmeow-linux-amd64.so main.go

# echo 'Build Linux ARM64'
# GOOS=linux GOARCH=arm64 CGO_ENABLED=1 go build -buildmode=c-shared -ldflags=-s -o ./whatsmeow/whatsmeow-linux-arm64.so main.go

echo 'Build for Linux 686'
GOOS=linux GOARCH=386 CGO_ENABLED=1 go build -buildmode=c-shared -o ./whatsmeow/whatsmeow-linux-686.so main.go

echo 'Build for Linux 386'
GOOS=linux GOARCH=386 CGO_ENABLED=1 go build -buildmode=c-shared -o ./whatsmeow/whatsmeow-linux-386.so main.go

