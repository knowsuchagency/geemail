from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from pathlib import Path
import smtplib


class Handler:
    """
    A simple context manager with which to send emails using gmail.

    """

    def __init__(self, from_: str, to: str, password: str):
        """
        :param from_: email of the sender
        :param to: email of the recipient
        :param password: the password for the sender's email
        """
        # configure server
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.SENDER = from_
        self.RECIPIENT = to
        self.PASSWORD = password

    def __enter__(self):
        self.server.starttls()
        self.server.login(self.SENDER, self.PASSWORD)
        return self

    def __exit__(self, *args):
        self.server.quit()

    def send(self, body: str, subject: str = None, attachments: [str] = None):
        """
        Send the email.

        :param body: The textual body of the email.
        :param subject: The optional subject of the email.
        :param attachments: Filepaths to attachments.
        """
        # create message
        msg = MIMEMultipart()
        msg['From'] = self.SENDER
        msg['To'] = self.RECIPIENT
        if subject is not None:
            msg['Subject'] = subject

        # set message body
        msg.attach(MIMEText(body, 'plain'))

        # attach content to message
        if attachments is not None:
            for attachment in attachments:
                # get absolute path to attachment
                path = Path(attachment).expanduser().absolute().__str__()

                with open(path, 'rb') as file_obj:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file_obj.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= {}".format(path))
                    msg.attach(part)

        # send it off
        self.server.sendmail(
            self.SENDER,
            self.RECIPIENT,
            msg.as_string(),
        )
