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
| Receive messages  | ✅ |
| Send image  | ✅ |
| Send media (audio/documents)  | soon!  |
| Send media (video)  | soon! |
| Send stickers | soon! |
| Receive media (images/audio/video/documents)  | ✅  |
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
| Linux ARM64  | ✅ |
| Linux 686  | ✅ |
| Linux 386  | ✅  |
| Windows amd64  | ✅  |
| Windows 32 bit  | soon! |
| OSX arm64  | soon! |
| OSX amd64  | soon! |

> ## Support this Project
> This project is maintained during my free time.
> If you'd like to support my work, please consider making a pull request to help fix any issues with the code.
> I would like to extend my gratitude to the open-source developers behind tls-client, tiktoken, and whatsmeow. Their work has inspired me greatly and helped me to create this project.