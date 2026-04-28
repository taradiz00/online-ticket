from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base
from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["argon2"], deprecated ="auto")

class User(Base):
    __tablename__ = "User"

    User_ID = Column(Integer, primary_key = True, autoincrement= True)
    Username = Column(String(250), nullable =False, unique= True)
    Password = Column(String(255), nullable= False)
    is_active = Column(Boolean, default=True)
    Email = Column(String(100), unique=True, nullable= False)
    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(DateTime, server_onupdate=func.now())
    phone_number = Column(String(20), nullable= True)
    Reset_Token =Column(String, nullable=True)
    Reset_Token_Expiry =Column(DateTime, nullable=True)
   
    reservations = relationship("Reservation", back_populates="users")
    tokens = relationship("TokenModel", back_populates="users")

    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)
    
    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.Password)
    
    def set_password(self, plain_password: str) -> None:
        self.Password = self.hash_password(plain_password)
