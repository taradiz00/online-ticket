from sqlalchemy import Column, Integer, String, CHAR, CheckConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class Airport(Base):
    __tablename__ = "Airport"

    Airport_ID = Column(Integer, primary_key=True, autoincrement=True)
    Airport_Name = Column(String(100), nullable=False, unique=True)
    Airport_Code = Column(CHAR(4), nullable=False, unique=True)
    Country_Name = Column(String(100), nullable=False)
    City_Name = Column(String(100), nullable=False)
    Airport_Contact_Number = Column(String(15), nullable=False)
    Airport_Capacity = Column(Integer)

    departing_flights = relationship("Flight", foreign_keys="Flight.origin_city_id ",back_populates="Origin_City")
    arriving_flights = relationship("Flight", foreign_keys="Flight.destination_city_id ",back_populates="Destination_City")
    

    __table_args__ = (
    CheckConstraint("Airport_Capacity >= 100000", name="chk_airport_capacity"),
)
