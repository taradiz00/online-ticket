from sqlalchemy import Column, Integer, String, CheckConstraint, Date, CHAR, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Passenger(Base):
    __tablename__ = "Passenger"

    Passenger_ID = Column(Integer, primary_key=True, autoincrement=True)
    Passenger_Name = Column(String(100), nullable=False)
    Passport_Number = Column(String(50), nullable=False, unique=True)
    Email = Column(String(100), nullable=False)
    Date_of_Birth = Column(Date)
    Gender = Column(CHAR(1))
    Phone_Number = Column(String(30))
    Reservation_ID = Column(Integer, ForeignKey("Reservation.Reservation_ID"))

    tickets = relationship("Ticket", back_populates="passengers")
    reservations = relationship("Reservation", back_populates="passengers")

    __table_args__ = (CheckConstraint( "Gender IN ('F', 'M')", name="chk_gender_valid"),) 