# WhatsFly
## Just run and have fun. Just try and go fly. 


WhatsApp web wrapper in Python. No selenium nor gecko web driver needed. 

setting up browser driver are tricky for python newcomers, and thus it makes your code soo laggy.

I knew that feeling. it was painful.

powered by Whatsmeow --a golang based WhatsApp library-- 'hopefully' will make this wrapper easy to use without sacrificing the speed and perfomance.

Thanks to Whatsmeow for amazing works. Inspired from tls-client, tiktoken, and whatsmeow.

## Installation

Install WhatsFly with pip

```bash
  pip install whatsfly
```

or :
```bash
  pip3 install --upgrade whatsfly
```

### *supported for linux amd64, linux 32bit and windows 64bit*
### *whatsmeow library for linux arm64, windows 32bit and macOS machines are not built yet*


## Usage/Examples

```javascript
from whatsfly import WhatsApp

chat = WhatsApp()
chat.send_message(message="Hello World!", phone="6283139750000")
```

## Supported features

| Feature  | Status |
| ------------- | ------------- |
| Multi Device  | ✅ |
| Send messages  | ✅ |
| Receive messages  | soon!  |
| Send media (images/audio/documents)  | soon!  |
| Send media (video)  | soon! |
| Send stickers | soon! |
| Receive media (images/audio/video/documents)  | soon!  |
| Send contact cards | soon! |
| Send location | soon! |
| Send buttons | soon! |
| Send lists | soon! |
| Receive location | soon! | 
| Message replies | soon! |
| Join groups by invite  | soon! |
| Get invite for group  | soon! |
| Modify group info (subject, description)  | soon!  |
| Modify group settings (send messages, edit info)  | soon!  |
| Add group participants  | soon!  |
| Kick group participants  | soon!  |
| Promote/demote group participants | soon! |
| Mention users | soon! |
| Mute/unmute chats | soon! |
| Block/unblock contacts | soon! |
| Get contact info | soon! |
| Get profile pictures | soon! |
| Set user status message | soon! |
| React to messages | soon! |

Something missing? Make an issue and let us know!

> ## Support my work
> This side project is maintained during my free time.\n
> Make a pull request and fix my bad code.
