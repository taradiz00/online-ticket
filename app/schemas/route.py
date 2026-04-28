from pydantic import BaseModel, ConfigDict
from datetime import time 
from decimal import Decimal

class RouteBase(BaseModel):
    Origin_Airport_Code: str
    Destination_Airport_Code: str
    Distance: Decimal
    Duration: time 


class RouteResponse(RouteBase):
    Flight_Route_ID: int
    Origin_Airport_Code: str
    Destination_Airport_Code: str
    Distance: Decimal
    Duration: time

    model_config = ConfigDict(from_attributes= True)