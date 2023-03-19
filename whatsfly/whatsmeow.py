"""
importing c shared whatsmeow library based on your machine.
broken code will be fixed soon.
"""

from sys import platform
from platform import machine
import ctypes
import os

# Load the shared library
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
    else:
        file_ext = '-linux-amd64.so'

root_dir = os.path.abspath(os.path.dirname(__file__))
lib = ctypes.CDLL(f'{root_dir}/dependencies/whatsmeow/whatsmeow{file_ext}')

# Define the Connect() and SendMessage() functions.
ClientConnect = lib.Connect
ClientConnect.argtypes = []
ClientConnect.restype = None

SendMessage = lib.SendMessage
SendMessage.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
SendMessage.restype = ctypes.c_int

SendImage = lib.SendImage
SendImage.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
SendImage.restype = ctypes.c_int