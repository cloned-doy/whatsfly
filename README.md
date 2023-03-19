# WhatsFly
## Just run and have fun. Just try and go fly. 

WhatsApp web wrapper in Python. No selenium nor gecko web driver needed. 

Setting up browser driver are tricky for python newcomers, and thus it makes your code so 'laggy'.

I knew that feeling. It's so painful.

So I make WhatsFly, implementing Whatsmeow --a golang based WhatsApp library. It will make his wrapper easy to use without sacrificing the speed and perfomance.

## Installation

```bash
  pip install whatsfly
```

or :
```bash
  pip install --upgrade whatsfly
```

## Usage/Examples

```javascript
from whatsfly import WhatsApp

chat = WhatsApp()

# send mesage
chat.send_message(phone="6283139750000", message="Hello World!")

# send image
chat.send_image(phone="6283139750000", image_path="path/to/image.jpg" caption="Hello World!")
```

## Features

| Feature  | Status |
| ------------- | ------------- |
| Multi Device  | ✅ |
| Send messages  | ✅ |
| Receive messages  | soon!  |
| Send image  | ✅ |
| Send media (audio/documents)  | soon!  |
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

## Supported machines

| Architecture  | Status |
| ------------- | ------------- |
| Linux amd64  | ✅ |
| Linux ARM64  | soon! |
| Linux 686  | ✅ |
| Linux 386  | ✅  |
| Windows amd64  | ✅  |
| Windows 32 bit  | soon! |
| OSX arm64  | soon! |
| OSX amd64  | soon! |

> ## Support my work
> This side project is maintained during my free time.
> Make a pull request and fix my bad code.
> Thank god, and thanks to all the opensource developers behind the tls-client, tiktoken, and whatsmeow.
