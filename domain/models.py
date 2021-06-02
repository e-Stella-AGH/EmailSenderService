from pydantic import BaseModel


class MailBody(BaseModel):
    subject: str
    sender: str
    receiver: str
    content: str
