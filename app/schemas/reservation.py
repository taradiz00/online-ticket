from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.passenger import PassengerCreate, PassengerResponse
from app.schemas.flight import FlightResponse

    


class ReservationCreate(BaseModel):
    Flight_ID: int
    passengers:list[PassengerCreate]



class ReservationResponse(BaseModel):
    Reservation_ID: int
    Reservation_Date: datetime
    flight: FlightResponse
    passengers: list[PassengerResponse]

    
    model_config = ConfigDict(from_attributes= True)