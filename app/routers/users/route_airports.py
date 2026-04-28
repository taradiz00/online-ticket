from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Airport
from app.schemas.airport import AirportResponse
from typing import List

router = APIRouter(
    prefix="/airports",
    tags=["Airports"]
)
 


@router.get("/airports/search", response_model=List[AirportResponse])
def search_airports_bycity(city: str = Query(..., min_length=2), db: Session = Depends(get_db)):
    airports = db.query(Airport).filter(Airport.City_Name.ilike(f"%{city}%")).all()
    if not airports:
        raise HTTPException(status_code=404, detail="City not found")
    return airports
