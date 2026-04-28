from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base



class TokenModel(Base):
    __tablename__ = "Tokens"

    tokens_id = Column(Integer, primary_key = True, autoincrement= True)
    token = Column(String(255), nullable =False, unique= True)
    created_date = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("User.User_ID"), nullable=False)
    
    users = relationship("User", back_populates="tokens")