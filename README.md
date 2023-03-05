# WhatsFly
## Just run and have fun. Just try and go fly. 

> ## Support my work
> Make a pull request and fix my bad code.

WhatsApp web wrapper in Python. No selenium nor gecko web driver needed. 

setting up browser driver are tricky for python newcomers, and thus it makes your code soo laggy.

i knew that feeling. it was painful.

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

### *linux arm64 and macOS machines are not supported yet*


## Usage/Examples

```javascript
from whatsfly import WhatsApp

chat = WhatsApp()
chat.send_message(message="Hello World!", phone="6283139750000")

