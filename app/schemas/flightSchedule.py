from pydantic import BaseModel, field_validator, ConfigDict
from datetime import time, date

class FlightScheduleBase(BaseModel):
    Frequency: str
    Effective_From: date
    Effective_To: date
    Arrival_Time: time
    Departure_Time: time
    Airline_ID: int
    Flight_Route_ID: int

    @field_validator("Effective_To")
    def check_effective_dates(cls, v, values):
        from_date = values.get("Effective_From")
        if from_date and v <= from_date:
            raise ValueError ("Effective To must be greater than Effective From")
        return v
        
    @field_validator("Departure_Time")
    def check_times(cls, v, values):
        arrival = values.get("Arrival_Time")
        if arrival and v == arrival:
            raise ValueError("Arrival Time and Departure Time cannot ne equal")
        return v



class FlightScheduleResponse(BaseModel):
    Flight_Schedule_ID: int
    Effective_From: date
    Effective_To: date
    Arrival_Time: time
    Departure_Time: time
    Airline_ID: int

    model_config = ConfigDict(from_attributes= True)