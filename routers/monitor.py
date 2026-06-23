from fastapi import APIRouter, Depends
from auth.token import get_current_user
from schemas.monitor import MonitorCreate
from app.database import get_db
from auth.token import get_current_user


router = APIRouter()

@router.post("/monitors")
def create_monitor(
    monitor : MonitorCreate,
    db = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_monitor = MonitorCreate(
        user_id = current_user.id,
        name = monitor.name,
        url = monitor.url,
        method = monitor.method,
        check_interval= monitor.check_interval,
        latency_threshold= monitor.latency_threshold,
        timeout_seconds= monitor.timeout_seconds
    )
    db.add(new_monitor)
    db.commit()
    db.refresh(new_monitor)

    return new_monitor