#!/bin/bash

# build and upload to twine script.
# this script help me build and upload the newer whatsfly code
echo "BUILD AND UPLOAD TO PYPI"
echo "from example dir move to whatsfly main dir"
cd ..

# Change directory to dependencies directory
echo "build the latest whatsmeow library first"
echo "Build library code for all machine"
cd whatsfly/dependencies
rm -f whatsmeow/whatsmeow-*
./build.sh

# Move up one directory
cd ../..
echo "update the pip sdist file and install"
# Activate my "test" virtual environment
source /home/doy/.local/bin/virtualenvwrapper.sh
workon test

# Run setup.py and pip install
python setup.py sdist
twine upload dist/*