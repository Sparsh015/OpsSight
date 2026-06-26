from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import query
from auth.token import get_current_user
from schemas.monitor import MonitorCreate, MonitorResponse, MonitorUpdate
from app.database import get_db
from auth.token import get_current_user
from models import Monitor

router = APIRouter()

@router.post("/monitors", response_model= MonitorResponse)
def create_monitor(
    monitor : MonitorCreate,
    db = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_monitor = Monitor(
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

@router.get("/monitors", response_model= list[MonitorResponse])
def get_monitors(
    current_user = Depends(get_current_user),
    db = Depends(get_db)
):
    monitors = db.query(Monitor).filter(
        Monitor.user_id == current_user.id
    ).all()

    return monitors

@router.get("/monitors/{monitor_id}", response_model= MonitorResponse)
def get_monitor(
    monitor_id : int,
    current_user = Depends(get_current_user),
    db = Depends(get_db)
):
    monitor = db.query(Monitor).filter(
        Monitor.id == monitor_id,
        Monitor.user_id == current_user.id
    ).first()

    if not monitor:
        raise HTTPException(
            status_code= 404,
            detail = "Monitor not found"
        )

    return monitor

@router.delete("/monitors/{monitor_id}", response_model= MonitorResponse)
def delete_monitor(
    monitor_id : int,
    current_user = Depends(get_current_user),
    db = Depends(get_db)
):
    monitor= db.query(Monitor).filter(
        Monitor.id == monitor_id,
        Monitor.user_id == current_user.id
    ).first()

    if not monitor:
        raise HTTPException(
            status_code=404,
            detail="Monitor not found"
        )

    db.delete(monitor)
    db.commit()

    return {
    "message": "Monitor deleted successfully"
    }

@router.put("/monitors/{monitor_id}", response_model= MonitorResponse)
def update_monitor(
    monitor_id : int,
    monitor: MonitorUpdate,
    db = Depends(get_db),
    current_user = Depends(get_current_user)
    ):
    existing_monitor = db.query(Monitor).filter(
        Monitor.id == monitor_id,
        Monitor.user_id == current_user.id
    ).first()

    if not existing_monitor:
        raise HTTPException(
            status_code= 404,
            detail = "Monitor not found"
        )
    
    existing_monitor.name = monitor.name
    existing_monitor.url = monitor.url
    existing_monitor.method = monitor.method
    existing_monitor.check_interval = monitor.check_interval
    existing_monitor.latency_threshold = monitor.latency_threshold
    existing_monitor.timeout_seconds = monitor.timeout_seconds
    existing_monitor.is_active = monitor.is_active

    db.commit()
    db.refresh(existing_monitor)
    return existing_monitor