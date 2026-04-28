from sqlalchemy import Column, Integer, String, Numeric, Time
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy import CHAR

class Flight_Route(Base):
    __tablename__ = "Flight_Route"

    Flight_Route_ID = Column(Integer, primary_key=True, autoincrement=True)
    Origin_Airport_code = Column(CHAR(4), nullable=False)
    Destination_Airport_Code = Column(CHAR(4), nullable=False)
    Distance = Column(Numeric(6,2), nullable=False)
    Duration = Column(Time)

    flights = relationship("Flight", back_populates="routes")
    flightschedules = relationship("FlightSchedule", back_populates="routes")