from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Airline(Base):
    __tablename__ = "Airline"

    Airline_ID = Column(Integer, primary_key=True, autoincrement=True)
    Airline_Name = Column(String(100), nullable=False, unique=True)
    Airline_Country = Column(String(50), nullable=False)
    Airline_Website = Column(String(100), nullable=False, unique=True)
    Airline_Contact_Number = Column(String(15), nullable=False)

    
    flightschedules = relationship("FlightSchedule", back_populates="airlines")
    flights = relationship("Flight", back_populates="Airlines")