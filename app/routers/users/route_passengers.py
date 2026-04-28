from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random
from app.models.reservation import Reservation
from app.core.database import get_db

from app.schemas.ticket_users import TicketResponse
from app.models import Flight
from app.models import Passenger
from app.models import Ticket


from faker import Faker

fake = Faker()

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']

def create_tick_class():
    classes = ['Economy', 'Business', 'First']
    class_type = random.choice(classes)
    return class_type


def create_reservation_date():
    reservation_date = fake.date_time_between(start_date='-1M', end_date='now')
    return reservation_date




@router.post("/passenger/{passenger_id}/confirm", response_model=TicketResponse)
def confirm_reservation(passenger_id:int, db: Session = Depends(get_db)):
    result = (
        db.query(Reservation, Passenger, Flight)
        .join(Passenger, Passenger.Reservation_ID == Reservation.Reservation_ID)
        .join(Flight, Flight.Flight_ID == Reservation.Flight_ID)
        .filter(Passenger.Passenger_ID == passenger_id)
        .first()
    )
    
    if not result:
        raise HTTPException(status_code=404, detail="Reservation / Passenger / Flight not found")
    reservation, passenger, flight = result 


    existing_ticket = db.query(Ticket).filter_by(Passenger_ID = passenger_id).first()
    if existing_ticket:
        raise HTTPException(status_code=400, detail="Ticket already exists")
    
    flight = reservation.flights
    
    while True:
        seat_num = str(random.randint(1,60)) + random.choice(letters) 
    
        existing_seat = db.query(Ticket).filter_by(Flight_ID = flight.Flight_ID, Seat_Number = seat_num).first()
        if not existing_seat:
            break
    

    ticket = Ticket(
        Reservation_ID = reservation.Reservation_ID,
        Ticket_Number = fake.unique.bothify('??-####'),
        Seat_Number = seat_num,
        Price = flight.Price,
        Class = create_tick_class(),
        Issue_Date = create_reservation_date(),
        Passenger_ID = passenger.Passenger_ID,
        Flight_ID = flight.Flight_ID
    )


    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket