from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from datetime import date
from enum import Enum


class GenderEnum(str, Enum):
    male = "M"
    female = "F"
    

        
class PassengerCreate(BaseModel): 
    Passenger_Name: str
    Email: EmailStr
    Phone_Number: str
    Passport_Number: str | None = None
    Date_of_Birth: date
    Gender: GenderEnum | None

    @field_validator("Date_of_Birth")
    @classmethod
    def check_age(cls, value: date):
        today = date.today()
        age = today.year - value.year -((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise ValueError("Passenger must be at least 18 years old to book a flight")
        return value


    

class PassengerResponse(BaseModel):
    Passenger_ID: int
    Passenger_Name: str
    Email: EmailStr
    Phone_Number: str
    Date_of_Birth: date
    
    model_config = ConfigDict(from_attributes= True)