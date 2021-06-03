from typing import Optional

from pydantic import BaseModel


class MailBody(BaseModel):
    subject: str
    sender_email: Optional[str] = "no-reply@e-stella.com"
    sender_name: Optional[str] = "No Reply"
    receiver: str
    content: str
