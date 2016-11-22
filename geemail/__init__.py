"""
Contains a context manager meant to make it easy to send emails with gmail.

Example:

from geemail import Handler

with Handler(sender_email, recipient_email, password) as h:
    h.send('Hello, world')
"""

__version__ = '0.1.1'

from .handler import Handler