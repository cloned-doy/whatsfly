#!/bin/bash

# this script help me test and run the newer whatsfly code
echo "RUN AND TEST THE LATEST WHATSFLY"
echo "from example dir move to whatsfly main dir"
cd ..

# Change directory to dependencies directory
echo "build the latest whatsmeow library first"
cd whatsfly/dependencies
rm -f whatsmeow/whatsmeow-*

# Build Golang code for my machine
echo "build for linux 686"
GOOS=linux GOARCH=386 CGO_ENABLED=1 go build -buildmode=c-shared -o ./whatsmeow/whatsmeow-linux-686.so main.go
cd ../..

echo "update the pip sdist file and install"
# Activate my "test" virtual environment
source /home/doy/.local/bin/virtualenvwrapper.sh
workon test

# Run setup.py and pip install
python setup.py sdist
pip install .

# Change directory and run examples/test.py
echo "back to example/test dir and run test.py"
cd examples
python test.py
