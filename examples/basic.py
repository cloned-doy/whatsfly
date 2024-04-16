from whatsfly import WhatsApp
import time

"""

basic usages

"""

def my_event_callback(event_data):
    ''' 
    simple event callback to listen to incoming event/messages. 
    whenever this function is called, it will retrieve the current incoming event or messages.
    '''
    print("Received event data:", event_data)

def listening_message(minutes):
    """ Stream messages for 'minutes' duration"""
    end_time = time.time() + minutes * 60  
    while time.time() < end_time:
        my_event_callback()
  
if __name__ == "__main__":

    phone = "6283139750000" # make sure to attach country code + phone number
    message = "Hello World!"

    whatsapp = WhatsApp(event_callback=my_event_callback)


    message_sent = whatsapp.send_message(phone=phone, message=message)
    
    listening_message(time=5)

    whatsapp.disconnect()