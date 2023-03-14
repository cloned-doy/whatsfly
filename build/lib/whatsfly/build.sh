#!/bin/sh

# This build.sh file was borrowed from https://github.com/bogdanfinn/tls-client/blob/master/cffi_dist/build.sh

# """ 
# make sure you have installed all build tools on your machine
# """

# echo 'Build OSX'
# GOOS=darwin GOARCH=arm64 go build -o ./dist/whatsmeow-darwin-arm64.dylib -buildmode=c-shared main.go
# GOOS=darwin GOARCH=amd64 go build -buildmode=c-shared -o ./dist/whatsmeow-darwin-amd64.dylib main.go

# rm -rf ~/.cache/go-build

echo 'Build for Linux Ubuntu'
GOOS=linux CGO_ENABLED=1 GOARCH=amd64 go build -buildmode=c-shared -ldflags=-s -o ./dist/whatsmeow-linux-amd64.so main.go

# echo 'Build Linux ARM64'
# GOOS=linux CGO_ENABLED=1 GOARCH=arm64 go build -buildmode=c-shared -ldflags=-s -o ./dist/whatsmeow-linux-arm64.so main.go

echo 'Build for Linux 686'
GOOS=linux CGO_ENABLED=1 GOARCH=386 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-686.so main.go

echo 'Build for Linux 386'
GOOS=linux CGO_ENABLED=1 GOARCH=386 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-386.so main.go

rm -rf ~/.cache/go-build

echo 'Build for Windows 32 Bit'
GOOS=windows GOARCH=386 CGO_ENABLED=1 CC=i686-w64-mingw32-gcc go build -buildmode=c-shared -o ./dist/whatsmeow-windows-32.dll main.go

echo 'Build for Windows amd64 Bit'
GOOS=windows GOARCH=amd64 CGO_ENABLED=1 CC=x86_64-w64-mingw32-gcc go build -buildmode=c-shared -o ./dist/whatsmeow-windows-64.dll main.go