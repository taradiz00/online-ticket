from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.schemas.users import *
from fastapi.responses import JSONResponse
import secrets
from app.auth.jwt_auth import generate_access_token, generate_refresh_token, decode_refresh_token



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def generate_token(length=32):
    return secrets.token_hex(length)   


@router.post("/login")
async def user_login(request:UserLogin, db:Session = Depends(get_db)):
    user_obj = db.query(User).filter_by(Username=request.Username.lower()).first()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    if not user_obj.verify_password(request.Password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    access_token = generate_access_token(user_obj.User_ID)
    refresh_token = generate_refresh_token(user_obj.User_ID)
    return JSONResponse(content={"detail":"Logged in successfully","access_token":access_token, "refresh_token":refresh_token})
    

@router.post("/register")
async def user_register(request:UserSignup, db:Session = Depends(get_db)):
    if db.query(User).filter_by(Username=request.Username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    user_obj = User(Username=request.Username,
                    Email=request.Email,
                    phone_number=request.phone_number,
                )
    user_obj.set_password(request.Password)
    db.add(user_obj)
    db.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"detail": "User registered successfully"})


@router.post("/refresh-token")
async def user_refresh_token(request:UserRefreshToken, db:Session = Depends(get_db)):
    user_id = decode_refresh_token(request.refresh_token)
    access_token = generate_access_token(user_id)
  
    return JSONResponse(content={"access_token": access_token}) 