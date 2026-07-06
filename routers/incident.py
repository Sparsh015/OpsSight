from fastapi import APIRouter, Depends, HTTPException
from models import Incident, Monitor
from auth.token import get_current_user
from app.database import get_db
from schemas.incident import IncidentResponse

router = APIRouter()

@router.get("/incidents", response_model=list[IncidentResponse])
def get_incidents(
    db = Depends(get_db),
    current_user = Depends(get_current_user),
):
    incidents = db.query(Incident).join(Monitor).filter(
        Monitor.user_id == current_user.id
    ).all()

    return incidents