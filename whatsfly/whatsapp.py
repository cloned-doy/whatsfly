# most of the API refs are not mine, thanks to https://github.com/mukulhase/WebWhatsapp-Wrapper
import os
import re
from typing import Optional
from .whatsmeow import new_whatsapp_client_wrapper, connect_wrapper, message_thread_wrapper, send_message_wrapper, send_image_wrapper
import ctypes
import json
import threading

"""
Basic WhatsApp features that I will developed soon:
    def get_all_chats(self):
    
    Fetches all chats
    :return: List of chats
    :rtype: list[Chat]
    
    return []

    def get_all_chat_ids(self):
    
    Fetches all chat ids
    :return: List of chat ids
    :rtype: list[str]
    
    return []

    def get_unread(
    self, include_me=False, include_notifications=False, use_unread_count=False
    ):
    
    Fetches unread messages
    :param include_me: Include user's messages
    :type include_me: bool or None
    :param include_notifications: Include events happening on chat
    :type include_notifications: bool or None
    :param use_unread_count: If set uses chat's 'unreadCount' attribute to fetch last n messages from chat
    :type use_unread_count: bool
    :return: List of unread messages grouped by chats
    :rtype: list[MessageGroup]
    
    unread_messages = []
    return unread_messages

    def get_unread_messages_in_chat(
    self, id, include_me=False, include_notifications=False
    ):
    
    I fetch unread messages from an asked chat.
    :param id: chat id
    :type  id: str
    :param include_me: if user's messages are to be included
    :type  include_me: bool
    :param include_notifications: if events happening on chat are to be included
    :type  include_notifications: bool
    :return: list of unread messages from asked chat
    :rtype: list
    
    # get unread messages
    # return them
    unread = []
    return unread

    def get_chat_from_phone_number(self, number, createIfNotFound=False):
    
    Gets chat by phone number
    Number format should be as it appears in Whatsapp ID
    For example, for the number:
    +972-51-234-5678
    This function would receive:
    972512345678
    :param number: Phone number
    :return: Chat
    :rtype: Chat
    
    return

    def send_media(self, path, chatid, caption):
    
        converts the file to base64 and sends it using the sendImage function of wapi.js
    :param path: file path
    :param chatid: chatId to be sent
    :param caption:
    :return:
    

    def send_video(self, message: str, phone: str, file_path: str):

    media_url = self.upload_media(phone, file_path)
    send_message = f"send video to {phone}: media url : {media_url}"

    return

    def get_contacts(self):
    
    Fetches list of all contacts
    This will return chats with people from the address book only
    Use get_all_chats for all chats
    :return: List of contacts
    :rtype: list[Contact]
    
    return []


    def send_message_with_thumbnail(self, path, chatid, url, title, description, text):
    
        converts the file to base64 and sends it using the sendImage function of wapi.js
    PS: The first link in text must be equals to url or thumbnail will not appear.
    :param path: image file path
    :param chatid: chatId to be sent
    :param url: of thumbnail
    :param title: of thumbnail
    :param description: of thumbnail
    :param text: under thumbnail
    :return:
    

    def chat_send_seen(self, chat_id):
    
    Send a seen to a chat given its ID
    :param chat_id: Chat ID
    :type chat_id: str
    
    return self.wapi_functions.sendSeen(chat_id)

    def check_number_status(self, number_id) -> bool:
    
    Check if a number is valid/registered in the whatsapp service
    :param number_id: number id
    :return:
    ""
    return True

    def subscribe_new_messages(self, observer):
    self.wapi_functions.new_messages_observable.subscribe(observer)

    def unsubscribe_new_messages(self, observer):
    self.wapi_functions.new_messages_observable.unsubscribe(observer)


    def is_connected(self) -> bool:
    "Returns if user's phone is connected to the internet.""
    # return self.wapi_functions.isConnected()
    return True

    def get_qr(self, filename=None):
    Get pairing QR code from client
    fn_png = 
    return fn_png

    def reload_qr(self):
    # self.driver.find_element_by_css_selector(self._SELECTORS["QRReloader"]).click()
    return

    def get_qr_base64(self):

    # return qr.screenshot_as_base64
    return
"""


class WhatsApp(object):
    def connect(self):
        connect_wrapper(self.c_WhatsAppClientId)

    def disconnect(self):
        disconnect_wrapper(self.c_WhatsAppClientId)

    def runMessageThread(self):
        message_thread_wrapper(self.c_WhatsAppClientId)

    def sendMessage(self, phone: str, message: str, group: bool = False):
        ret = send_message_wrapper(self.c_WhatsAppClientId, phone.encode(), message.encode(), group)
    
    def sendImage(self, phone: str, image_path: str, caption: str = "", group: bool = False):
        send_image_wrapper(self.c_WhatsAppClientId, phone.encode(), image_path.encode(), caption.encode(), group)

    def __init__(self, phone_number: str = "", media_path: str = "", user: Optional[str] = None, machine: str = "mac", browser: str = "safari", on_event = None, on_disconnect = None):
        """
        user : user phone number. in the whatsmeow golang are called client.
        machine : os login info
        browser : browser login info
        import the compiled whatsmeow golang package, and setup basic client and database.
        auto run based on any database (login and chat info database), hence a user phone number are declared.
        if there is no user login assigned yet, assign a new client.
        put the database in current file whereever this class instancess are imported. database/client.db
        """
        self.user 	 = user
        self.user_name = None
        self.machine = machine
        self.browser = browser
        self.wapi_functions = browser
        self.connected = None

        if media_path:
            if not os.path.exists(media_path):
                os.makedirs(media_path)
            for subdir in ["images", "audios", "videos", "documents", "stickers"]:
                full_media_path = media_path + "/" + subdir
                if not os.path.exists(full_media_path):
                    os.makedirs(full_media_path)

        def on_event_json(s):
            try:
                s = s.decode()
            except:
                pass
            try:
                s = json.loads(s)
            except:
                pass
            on_event(s)

        CMPFUNC_NONE_STR = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
        CMPFUNC_NONE = ctypes.CFUNCTYPE(None)

        self.C_ON_EVENT = CMPFUNC_NONE_STR(on_event_json) if callable(on_event) else ctypes.cast(None, CMPFUNC_NONE_STR)
        self.C_ON_DISCONNECT = CMPFUNC_NONE(on_disconnect) if callable(on_disconnect) else ctypes.cast(None, CMPFUNC_NONE)

        self.c_WhatsAppClientId = new_whatsapp_client_wrapper(
            phone_number.encode(),
            media_path.encode(),
            self.C_ON_DISCONNECT,
            self.C_ON_EVENT
        )

if __name__ == '__main__':
    client = WhatsApp()
    message = "Hello World!"
    phone = "6283139000000"
    client.send_message(message=message, phone=phone)
