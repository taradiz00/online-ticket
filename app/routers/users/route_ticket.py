from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Ticket
from app.schemas.ticket_users import TicketResponse


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)



@router.get("/ticket/{ticket_id}", response_model=TicketResponse)
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter_by(Ticket_ID=ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket

