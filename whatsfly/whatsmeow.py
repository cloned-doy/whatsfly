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

new_whatsapp_client_wrapper = lib.NewWhatsAppClientWrapper
new_whatsapp_client_wrapper.argstype = [ctypes.c_char_p, ctypes.c_char_p, ctypes.CFUNCTYPE(None), ctypes.CFUNCTYPE(None, ctypes.c_char_p)]
new_whatsapp_client_wrapper.restype = ctypes.c_int

connect_wrapper = lib.ConnectWrapper
connect_wrapper.argstype = [ctypes.c_int]

disconnect_wrapper = lib.DisconnectWrapper
disconnect_wrapper.argstype = [ctypes.c_int]

message_thread_wrapper = lib.MessageThreadWrapper
message_thread_wrapper.argstype = [ctypes.c_int]

send_message_wrapper = lib.SendMessageWrapper
send_message_wrapper.argstype = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]

send_image_wrapper = lib.SendImageWrapper
send_image_wrapper.argstype = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
