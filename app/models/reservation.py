from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.dialects.mssql import DATETIME2

class Reservation(Base):
    __tablename__ = "Reservation"

    Reservation_ID = Column(Integer, primary_key=True, autoincrement=True)
    Reservation_Date = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(tz=timezone.utc))
    User_ID = Column(Integer, ForeignKey("User.User_ID"))
    Flight_ID = Column(Integer, ForeignKey("Flight.Flight_ID"))

    users = relationship("User", back_populates="reservations")
    flights = relationship("Flight", back_populates="reservations")
    passengers = relationship("Passenger", back_populates="reservations")
    tickets = relationship("Ticket",back_populates="reservations")


