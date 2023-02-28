# WhatsFly
## Just run and have fun. Just try and go fly. 

### *current version 0.0.1 works in linux 32bit only*

WhatsApp web wrapper in Python. No selenium or gecko web driver needed. 

setting up browser driver are tricky for python newcomers, and thus it makes your code soo laggy.

i knew that feeling. it was painful.

powered by Whatsmeow --a golang based WhatsApp library-- 'hopefully' will make this wrapper easy to use without sacrificing the speed and perfomance.

Thanks to Whatsmeow for amazing works. Inspired from tls-client, tiktoken, and whatsmeow.

## Installation

Install WhatsFly with pip

```bash
  pip install whatsfly
```

## *except for linux 32bit, please first compile whatsfly/dependencies/main.go based on your machine*




## Usage/Examples

```javascript
from whatsfly import WhatsApp

chat = WhatsApp()
chat.send_message(message="Hello World!", phone="6283139750000")

