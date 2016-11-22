# geemail

A dead simple library to send emails using gmail in Python 3.

## Installation

`pip install geemail`

## Usage

```python
from geemail import Handler

with Handler(sender_email, recipient_email, password) as h:
    h.send('Hello, world')
```

