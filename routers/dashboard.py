from fastapi import APIRouter, Depends

from app.database import get_db
from auth.token import get_current_user

from models import Monitor, Incident, CheckResult
from sqlalchemy import func

router = APIRouter()

@router.get("/dashboard")
def get_dashboard(
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    total_monitors = db.query(Monitor).filter(
        Monitor.user_id == current_user.id
    ).count()

    active_incidents = db.query(Incident).join(Monitor).filter(
        Monitor.user_id == current_user.id,
        Incident.resolved == False
    ).count()

    average_response_time = db.query(func.avg(CheckResult.response_time)).join(
        Monitor).filter(
            Monitor.user_id == current_user.id,
            CheckResult.response_time is not None
        ).scalar()

    total_checks = db.query(CheckResult).join(
        Monitor).filter(
            Monitor.user_id == current_user.id
        ).count()

    successful_checks = db.query(CheckResult).join(
        Monitor).filter(
            Monitor.user_id == current_user.id,
            CheckResult.is_success == True
        ).count()

    uptime_percentage = ((successful_checks / total_checks) * 100 
    if total_checks > 0 else 0)
    
    return {
        "total_monitors": total_monitors,
        "active_incidents": active_incidents,
        "average_response_time": average_response_time,
        "uptime_percentage": uptime_percentage
    }