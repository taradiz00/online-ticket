from pydantic import BaseModel, ConfigDict


class AirlineBase(BaseModel):
    Airline_Name: str
    Airline_Country: str
    Airline_Website: str
    Airline_Contact_Number: str


    model_config = ConfigDict(from_attributes=True)


class AirlineResponse(BaseModel):
    Airline_ID: int
    
    Airline_Name: str
    Airline_Country: str
    Airline_Website: str
    Airline_Contact_Number: str
    
    model_config = ConfigDict(from_attributes=True)