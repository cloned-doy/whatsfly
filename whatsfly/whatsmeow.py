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
    file_ext = '-arm64.dylib' if machine() == "arm64" else '-x86.dylib'
elif platform in ('win32', 'cygwin'):
    file_ext = '-64.dll' if 8 == ctypes.sizeof(ctypes.c_voidp) else '-32.dll'
else:
    if machine() == "aarch64":
        file_ext = '-arm64.so'
    elif "x86" in machine():
        file_ext = '-x86.so'
    elif "i686" in machine():
    	file_ext = 'i386.so'
    else:
        file_ext = '-amd64.so'

root_dir = os.path.abspath(os.path.dirname(__file__))

# Load the shared library
lib = ctypes.CDLL(f'{root_dir}/dependencies/libwapp.so')

# Define the Connect function
ClientConnect = lib.Connect
ClientConnect.argtypes = []
ClientConnect.restype = None

# Define the argument and return types of the SendMessage function
SendMessage = lib.SendMessage
SendMessage.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SendMessage.restype = ctypes.c_int