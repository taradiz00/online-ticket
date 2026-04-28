from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import User
import secrets
from datetime import datetime, timedelta, timezone
from app.core.email_util import send_reset_email
import os


router = APIRouter(
    prefix="/password",
    tags=["Password"]
)


@router.post("/forgot-password")
def forget_password(email: str, db: Session = Depends(get_db)):

    user = db.query(User).filter_by(Email=email).first()

    if not user:
        return {"message": "If this email exists, reset link sent"}
    
    token = secrets.token_urlsafe(32)

    user.Reset_Token = token
    user.Reset_Token_Expiry = datetime.now(timezone.utc) + timedelta(minutes=15)

    db.commit()

    BASE_URL = os.getenv("BASE_URL")
    reset_link = f"{BASE_URL}/reset-password?token={token}"

    send_reset_email(user.Email, reset_link)

    return {"message": "Reset link sent to email"}





@router.post("/reset-password")
def forget_password(token: str, new_password: str, db: Session = Depends(get_db)):

    user = db.query(User).filter_by(Reset_Token =token).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    
    if user.Reset_Token_Expiry < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Token expired")
    
    user.set_password(new_password)

    user.Reset_Token = None
    user.Reset_Token_Expiry = None

    db.commit()

    return {"message": "Password reset successfully"} 