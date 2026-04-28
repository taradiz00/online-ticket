from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, aliased, joinedload
from datetime import date
from app.core.database import get_db
from app.models.flight import Flight
from app.models.airport import Airport
from app.models.airline import Airline
from app.schemas.flight import  FlightResponse
from typing import List


router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


@router.get("/search/flights", response_model=List[FlightResponse])
def search_flights(origin_city: str = Query(...,min_length=2),
                   destination_city:str = Query(...,min_length=2),
                   departure_date:date = Query(...),
                    db: Session = Depends(get_db)):
    OriginCity = aliased(Airport)
    DesCity = aliased(Airport)

    flights = (
        db.query(Flight)
        .join(OriginCity, Flight.origin_city_id == OriginCity.Airport_ID)
        .join(DesCity, Flight.destination_city_id == DesCity.Airport_ID)
        .join(Airline, Flight.Airline_ID == Airline.Airline_ID)
        .options(
            joinedload(Flight.Origin_City),
            joinedload(Flight.Destination_City),
            joinedload(Flight.Airlines)
        )
        .filter(
            OriginCity.City_Name.ilike(origin_city),
            DesCity.City_Name.ilike(destination_city),
            Flight.Departure_Time >= departure_date
        )
        .all()
    )
    response =[
        FlightResponse(
            Flight_ID = f.Flight_ID,
            Destination_City =f.Destination_City.City_Name,
            Origin_City = f.Origin_City.City_Name,
            Airline_Name = f.Airlines.Airline_Name,
            Departure_Time= f.Departure_Time,
            Arrival_Time= f.Arrival_Time,
            Price= f.Price,
            Flight_Number = f.Flight_Number
        )
        for f in flights
    ]
    return response