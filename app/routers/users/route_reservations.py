from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random
from app.models.reservation import Reservation
from app.core.database import get_db
from app.schemas.reservation import ReservationResponse
from app.schemas.passenger import PassengerCreate, PassengerResponse
from app.schemas.flight import FlightResponse
from app.models import User
from app.models import Flight
from app.models import Passenger
from app.models import Ticket
from datetime import datetime, timezone
from app.auth.jwt_auth import get_authenticated_user
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

    

@router.post("/reservation/init", response_model=ReservationResponse)
def init_reservation(flight_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_authenticated_user)):
    flight = db.query(Flight).filter(Flight.Flight_ID == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    
    new_reservation = Reservation(
        User_ID = current_user.User_ID,
        Flight_ID = flight.Flight_ID,
        Reservation_Date = datetime.now(tz=timezone.utc)
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    flight_response = FlightResponse(
        Flight_ID=flight.Flight_ID,
        Origin_City=flight.Origin_City.City_Name,
        Destination_City=flight.Destination_City.City_Name,
        Airline_Name=flight.Airlines.Airline_Name,
        Price= flight.Price,
        Flight_Number=flight.Flight_Number,
        Departure_Time=flight.Departure_Time,
        Arrival_Time=flight.Arrival_Time

    )    

    return ReservationResponse(
        Reservation_ID= new_reservation.Reservation_ID,
        Reservation_Date= new_reservation.Reservation_Date,
        flight=flight_response,
        passengers=[]
    )

@router.post("/reservation/{reservation_id}/add_passengers", response_model = ReservationResponse)
def add_passengers(reservation_id: int, passengers: list[PassengerCreate], db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.Reservation_ID == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    
    for p in passengers:
        passenger_obj = Passenger (
            Reservation_ID = reservation.Reservation_ID,
            Passenger_Name = p.Passenger_Name,
            Email = p.Email,
            Phone_Number = p.Phone_Number,
            Passport_Number = p.Passport_Number,
            Gender = p.Gender,
            Date_of_Birth = p.Date_of_Birth
        )
        db.add(passenger_obj)
    db.commit()
    db.refresh(reservation)

    flight_response = FlightResponse(
        Flight_ID=reservation.flights.Flight_ID,
        Origin_City=reservation.flights.Origin_City.City_Name,
        Destination_City=reservation.flights.Destination_City.City_Name,
        Airline_Name=reservation.flights.Airlines.Airline_Name,
        Price= reservation.flights.Price,
        Flight_Number=reservation.flights.Flight_Number,
        Departure_Time=reservation.flights.Departure_Time,
        Arrival_Time=reservation.flights.Arrival_Time

    )

    passenger_responses= [
        PassengerResponse(
            Passenger_ID=p.Passenger_ID,
            Passenger_Name=p.Passenger_Name,
            Email= p.Email,
            Phone_Number=p.Phone_Number,
            Date_of_Birth=p.Date_of_Birth
        )
        for p in reservation.passengers
    ]

    return ReservationResponse(
        Reservation_ID = reservation.Reservation_ID,
        Reservation_Date = reservation.Reservation_Date,
        flight = flight_response,
        passengers= passenger_responses
    )
    