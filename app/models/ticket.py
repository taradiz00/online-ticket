from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class Ticket(Base):
    __tablename__ = "Ticket"

    Ticket_ID = Column(Integer, primary_key=True, autoincrement=True)
    Ticket_Number = Column(String(20), nullable=False)
    Seat_Number = Column(String(5), nullable=False)
    Class= Column(String(15), nullable=False)
    Issue_Date = Column(DateTime)
    Price = Column(Numeric(10,2), nullable=False)
    Reservation_ID = Column(Integer, ForeignKey("Reservation.Reservation_ID"), nullable=False)
    Passenger_ID = Column(Integer, ForeignKey("Passenger.Passenger_ID"), nullable=False)
    Flight_ID = Column(Integer, ForeignKey("Flight.Flight_ID"), nullable=False)

    passengers = relationship("Passenger", back_populates="tickets")
    reservations = relationship("Reservation",back_populates="tickets")
    flights = relationship("Flight", back_populates="tickets")

    __table_args__ = (
        CheckConstraint("(Class IN ('Economy', 'Business', 'First')", name="chk_cls_type"),
    )