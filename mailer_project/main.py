from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
import smtplib

app = FastAPI()

class Email(BaseModel):
    to: EmailStr
    subject: str
    message: str

@app.post("/send_email")
def send_email(email: Email):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your-email@gmail.com", "your-password")
        server.sendmail("your-email@gmail.com", email.to, f"Subject: {email.subject}\n\n{email.message}")
        server.quit()
        return {"message": "Email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
