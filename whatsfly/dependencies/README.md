# Building main.go

This repository is currently in the development phase. If your machine is not yet supported, you can still compile the `main.go` file on your own.

Simply take a look to the `build.sh` file for how each code compiled for each machines.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have installed all the necessary build tools on your machine.

3. Supposed you using an ubuntu machine and want to compile for all machines:
     ```
     sudo apt-get install gcc-multilib linux-libc-dev gcc-mingw-w64-x86-64 libc6-dev 
     ```
     *when gcc-multilib is installed, compiling for linux ARM need to do a separated install: gcc-aarch64-linux-gnu*
     *consider to install linux-libc-dev:i386 for compiling 32bit machine*

4. Once the build tools are installed, navigate to the repository directory and execute the `./build.sh all` script.

## Acknowledgements

The `build.sh` file used in this repository was borrowed from [bogdanfinn/tls-client](https://github.com/bogdanfinn/tls-client/blob/master/cffi_dist/build.sh).