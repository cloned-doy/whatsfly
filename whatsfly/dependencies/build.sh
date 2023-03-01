#!/bin/sh

# This build.sh file was borrowed from https://github.com/bogdanfinn/tls-client/blob/master/cffi_dist/build.sh

echo 'Build OSX'
GOOS=darwin CGO_ENABLED=1 GOARCH=arm64 go build -buildmode=c-shared -o ./dist/whatsmeow-darwin-arm64.dylib
GOOS=darwin CGO_ENABLED=1 GOARCH=amd64 go build -buildmode=c-shared -o ./dist/whatsmeow-darwin-amd64.dylib

echo 'Build Linux ARM64'
GOOS=linux CGO_ENABLED=1 GOARCH=arm64 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-arm64.so

echo 'Build Linux 686'
GOOS=linux CGO_ENABLED=1 GOARCH=386 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-686.so

echo 'Build Linux 386'
GOOS=linux CGO_ENABLED=1 GOARCH=386 GO386=387 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-386.so

echo 'Build Linux Ubuntu'
GOOS=linux CGO_ENABLED=1 GOARCH=amd64 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-amd64.so

echo 'Build Windows 32 Bit'
GOOS=windows CGO_ENABLED=1 GOARCH=386 go build -buildmode=c-shared -o ./dist/whatsmeow-windows-32.dll

echo 'Build Windows 64 Bit'
GOOS=windows CGO_ENABLED=1 GOARCH=amd64 go build -buildmode=c-shared -o ./dist/whatsmeow-windows-64.dll

echo 'Build Linux ARMv7'
GOOS=linux CGO_ENABLED=1 GOARCH=arm GOARM=7 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-armhf.so

echo 'Build Linux ARMv8'
GOOS=linux CGO_ENABLED=1 GOARCH=arm64 go build -buildmode=c-shared -o ./dist/whatsmeow-linux-armv8.so
