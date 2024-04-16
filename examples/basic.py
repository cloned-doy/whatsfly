from whatsfly import WhatsApp

"""

basic usages

"""

whatsapp = WhatsApp()

def my_event_callback(event_data):
    ''' this is an example to listen to incoming messages. '''
    print("Received event data:", event_data)

whatsapp = WhatsApp(event_callback=my_event_callback)

phone = "6283139750000" # make sure to attach country code + phone number
message = "Hello World!"

print(f"send message : {send_msg}")
response = whatsapp.send_message(phone=phone, message=message)

# listening to incoming messages
while True:
    my_event_callback()