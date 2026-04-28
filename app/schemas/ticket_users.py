from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal

class TicketResponse(BaseModel):
    Ticket_ID: int
    Ticket_Number: str
    Seat_Number: str
    Class: str
    Issue_Date: datetime
    Price: Decimal
    Reservation_ID: int
    Passenger_ID: int
    Flight_ID: int

    model_config = ConfigDict(from_attributes= True)