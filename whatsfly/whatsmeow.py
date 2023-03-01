"""
import whatsmeow c shared here

broken code

will be fixed soon

"""

from sys import platform
from platform import machine
import ctypes
import os

if platform == 'darwin':
    file_ext = '-darwin-arm64.dylib' if machine() == "arm64" else '-darwin-amd64.dylib'
elif platform in ('win32', 'cygwin'):
    file_ext = '-windows-64.dll' if 8 == ctypes.sizeof(ctypes.c_voidp) else '-windows-32.dll'
else:
    machine = machine()
    if machine == "aarch64":
        file_ext = '-linux-arm64.so'
    elif machine.startswith("i686"):
        file_ext = '-linux-686.so'
    elif machine.startswith("i386"):
        file_ext = '-linux-386.so'
    elif machine.startswith("armv7"):
        file_ext = '-linux-armhf.so'
    elif machine.startswith("armv8"):
        file_ext = '-linux-armv8.so'
    else:
        file_ext = '-linux-amd64.so'

root_dir = os.path.abspath(os.path.dirname(__file__))
lib = ctypes.CDLL(f'{root_dir}/dependencies/dist/whatsmeow{file_ext}')
# Load the shared library
# lib = ctypes.CDLL(f'{root_dir}/dependencies/libwapp.so')

# Define the Connect function
ClientConnect = lib.Connect
ClientConnect.argtypes = []
ClientConnect.restype = None

# Define the argument and return types of the SendMessage function
SendMessage = lib.SendMessage
SendMessage.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SendMessage.restype = ctypes.c_int