import smtplib
from typing import Optional

from fastapi import FastAPI, HTTPException, Header

from domain.models import MailBody
from infrastructure.EmailSender import send

app = FastAPI()


@app.get("/")
async def hello():
    return {
        "hello": "hello"
    }


@app.post("/email", status_code=200)
async def send_email(email: MailBody, x_dry_run: Optional[str] = Header("False")):
    if x_dry_run == "True":
        return {
            "mail": email
        }
    try:
        send(email)
    except smtplib.SMTPException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Mail server error, {e}"
        )
    return {
        "mail_status": "sent"
    }
