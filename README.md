# geemail

A dead simple library to send emails using gmail in Python 3.

## Installation

`pip install geemail`

## Usage

Handler is a context manager with only one method, **send**.

```python
send(self, body: str, subject: str = None, attachments: [str] = None)
```


```python
from geemail import Handler

with Handler(sender_email, recipient_email, password) as h:
    h.send('Hello, world') # send an email with blank subject and 'Hello, world' as the body
    h.send('help', subject="I've fallen and I can't get up") # body is 'help' and subject is "I've fallen and I can't get up"
    h.send('Check out these cat pictures', attachments=['path/to/a/picture', 'or/two']) # body is 'Check out these cat pictures' and has attachments, but subject will be blank
```

