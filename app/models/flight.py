from sqlalchemy import Column, Integer, String, CheckConstraint, ForeignKeyConstraint, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.dialects.mssql import DATETIME2

class Flight(Base):
    __tablename__ = "Flight"

    Flight_ID = Column(Integer, primary_key=True, autoincrement=True)
    Flight_Number = Column(String(10), nullable=False) 
    Arrival_Time = Column(DATETIME2, nullable=False)
    Departure_Time = Column(DATETIME2, nullable=False)
    FlightStatus = Column(String(10), server_default='Scheduled', nullable=False)
    Price = Column(Numeric(10,2), nullable=True)
    FLightSchedule_ID = Column(Integer, ForeignKey("FlightSchedule.FlightSchedule_ID"), nullable=False)
    Flight_Route_ID = Column(Integer, ForeignKey("Flight_Route.Flight_Route_ID"), nullable=False)
    Gate_Number = Column(Integer, nullable=False)
    Terminal_Number = Column(Integer, nullable=False)
    Airport_ID = Column(Integer, ForeignKey("Airport.Airport_ID"), nullable=False)
    Airline_ID = Column(Integer, ForeignKey("Airline.Airline_ID"), nullable= False)
    origin_city_id = Column(Integer, ForeignKey("Airport.Airport_ID"))
    destination_city_id = Column(Integer, ForeignKey("Airport.Airport_ID"))

    Origin_City = relationship("Airport", foreign_keys=[origin_city_id], back_populates="departing_flights")
    Destination_City = relationship("Airport", foreign_keys=[destination_city_id], back_populates="arriving_flights")
    Airlines = relationship("Airline", back_populates="flights")
    reservations = relationship("Reservation", back_populates="flights")
    tickets = relationship("Ticket", back_populates="flights")
    flightschedules = relationship("FlightSchedule", back_populates="flights")
    routes = relationship("Flight_Route", back_populates="flights")
  

    __table_args__ = (
        CheckConstraint(
        "FlightStatus IN ('Scheduled', 'Boarding', 'Delayed', 'Departed', 'Landed', 'Cancelled')",
        name="chk_flightstatus_valid"
    ),
        # ForeignKeyConstraint(
        #     ["Terminal_Number", "Airport_ID", "Gate_Number"],
        #     ["Gate.Terminal_Number", "Gate.Airport_ID", "Gate.Gate_Number"],
        #     name="fk_flight_gate"
        # )
    )