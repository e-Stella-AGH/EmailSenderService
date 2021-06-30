import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from domain.models import MailBody
import os

try:
    from local_auth import login, password
except ImportError:
    login, password = os.environ["EMAIL_LOGIN"], os.environ["EMAIL_PASSWORD"]


def send(email: MailBody):
    msg = MIMEMultipart()
    msg['Subject'] = email.subject
    msg['From'] = f"{email.sender_name} <{email.sender_email}>"
    msg['To'] = email.receiver
    msg.attach(MIMEText(email.content))
    msg.add_header("reply-to", email.sender_email)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(login, password)
    server.sendmail(login, email.receiver, msg.as_string())
    server.close()
    return "Successfully sent email"
