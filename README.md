# geemail

A dead simple library to send emails using gmail in Python 3.

## Installation

`pip install geemail`

## Usage

Handler is a context manager which will close itself which finished sending stuff.

It has only one method, send, with the following function signature:
```python
send(self, body: str, subject: str = None, attachments: [str] = None)
```


```python
from geemail import Handler

with Handler(sender_email, recipient_email, password) as h:
    # the
    h.send('Hello, world')
```

