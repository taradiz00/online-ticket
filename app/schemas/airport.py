from pydantic import BaseModel, ConfigDict

class AirportBase(BaseModel):
    Airport_Name: str
    Airport_Code: str
    Country_Name: str
    City_Name: str
    Capacity: int
    Contact_Number: str


class AirportResponse(BaseModel):
    Airport_ID: int
    Airport_Name: str
    Airport_Code: str
    Country_Name: str
    City_Name: str

    model_config = ConfigDict(from_attributes=True)