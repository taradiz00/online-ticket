from pydantic import BaseModel, EmailStr, field_validator, ConfigDict, Field
from datetime import date, datetime
import re
from typing import Optional
from enum import Enum

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"


class UserCreate(BaseModel):
    Password: str = Field(...,description="password of the user")
    Username: str = Field(...,max_length=250, description="username of the user")
    Email: EmailStr
    Password_confirm: str = Field(...,description="confirm password of the user")
    phone_number: Optional[str] = None
    gender: Optional[GenderEnum] = None
    full_name: str
    date_of_birth: date
    

    @field_validator("Password")
    @classmethod
    def validate_pwd(cls, value: str):
        if len(value)<6:
            raise ValueError("Password must be at least 6 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must have at least 1 uppercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must have at least 1 number")
        return value

class UserLogin(BaseModel):
    Password: str = Field(...,description="password of the user")
    Username: str = Field(...,max_length=250, description="username of the user")


class UserUpdate(BaseModel):
    Password: str = Field(...,description="password of the user")
    Username: str = Field(...,max_length=250, description="username of the user")


class UserSignup(BaseModel):
    Username: str = Field(...,max_length=250, description="username of the user")
    Email: EmailStr
    phone_number: Optional[str] = None
    Password: str = Field(..., min_length= 6, max_length=64, description="password of the user")
    Password_Confirm: str = Field(...,description="confirm password of the user")
    
    @field_validator("Password")
    @classmethod
    def validate_pwd(cls, value: str): 
        if len(value)<6:
            raise ValueError("Password must be at least 6 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must have at least 1 uppercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must have at least 1 number")
        return value
    
    @field_validator("Password_Confirm")
    @classmethod
    def check_passwords_match(cls,v: str,info):
        if v != info.data.get("Password"):
            raise ValueError("Passwords don't match")
        return v


class UserResponse(BaseModel):
    User_ID: int
    is_active: bool
    created_date: datetime
    updated_date: datetime
    Username: str
    Email: EmailStr
    full_name: str

    model_config = ConfigDict(from_attributes= True)


class UserRefreshToken(BaseModel):
    refresh_token: str = Field(...,description="refresh token of the user")
    Username: str = Field(...,max_length=250, description="username of the user")
    Email: EmailStr
    Password_Confirm: str = Field(...,description="confirm password of the user")
    phone_number: Optional[str] = None
    gender: Optional[GenderEnum] = None
    full_name: str
    date_of_birth:date