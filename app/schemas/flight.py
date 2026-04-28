from pydantic import BaseModel, field_validator, ConfigDict
from decimal import Decimal
from datetime import datetime


class FlightBase(BaseModel):
     Flight_Number: str
     Arrival_Time: datetime
     Departure_Time: datetime
     Flight_Status: str
     FLightSchedule_ID: int
     Aircraft_ID: int
     Flight_Route_ID: int
     Airport_ID: int

     @field_validator("Flight_Status")
     def validate_status(cls, value):
        allowed = ["'Scheduled', 'Boarding', 'Delayed', 'Departed', 'Landed', 'Cancelled'"]
        if value not in allowed:
            raise ValueError("Flight status must be in the allowed list")
        return value


	
class FlightResponse(BaseModel):
    Flight_ID: int
    Origin_City: str
    Destination_City: str
    Airline_Name: str
    Price: Decimal
    Flight_Number: str
    Departure_Time: datetime
    Arrival_Time: datetime

    model_config = ConfigDict(from_attributes=True)