import ctypes

# Load the shared library
lib = ctypes.CDLL('./libwapp.so')

# Define the Connect function
lib.Connect.argtypes = []
lib.Connect.restype = None

# Define the argument and return types of the SendMessage function
lib.SendMessage.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.SendMessage.restype = ctypes.c_int

# Call the Connect function
lib.Connect()

# Call the SendMessage function with a phone number and a message
number = "6283139755157"
message = "Hello, World!"
result = lib.SendMessage(number.encode(), message.encode())


message = "Hala Madrid, World!"
result2 = lib.SendMessage(number.encode(), message.encode())


message = "Takbirrr, World!"

result3 = lib.SendMessage(number.encode(), message.encode())

if result == 0:
    print("Message sent successfully")
else:
    print("Failed to send message")

if result2 == 0:
    print("Message sent successfully")
else:
    print("Failed to send message")

if result3 == 0:
    print("Message sent successfully")
else:
    print("Failed to send message")

