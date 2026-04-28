from sqlalchemy import Column, Integer, String, DateTime, Time, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy import Date

class FlightSchedule(Base):
    __tablename__ = "FlightSchedule"

    FlightSchedule_ID = Column(Integer, primary_key=True, autoincrement=True)
    Frequency = Column(String(20), nullable=False)
    Effective_From = Column(Date, nullable=False)
    Effective_To = Column(Date, nullable=False)
    Arrival_Time = Column(Time, nullable=False)
    Departure_Time = Column(Time, nullable=False)
    Airline_ID = Column(Integer, ForeignKey("Airline.Airline_ID"), nullable=False)
    Flight_Route_ID = Column(Integer, ForeignKey("Flight_Route.Flight_Route_ID"), nullable=False)

    airlines = relationship("Airline", back_populates="flightschedules")
    flights = relationship("Flight", back_populates="flightschedules")
    routes = relationship("Flight_Route", back_populates="flightschedules")

    __table_args__ = (
        CheckConstraint(
    "Frequency IN ('Daily', 'Weekly', 'Monthly')",
    name="chk_frqnc"
),
        CheckConstraint("Effective_To > Effective_From", name="chk_eff"),
        CheckConstraint("Arrival_Time <> Departure_Time", name = "chl_arr_dep")
    )