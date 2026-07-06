from fastapi import APIRouter, Depends, HTTPException
from models import Monitor, CheckResult
from auth.token import get_current_user
from app.database import get_db
import httpx
import time
from schemas.check_result import CheckResultResponse
from services.monitor_service import perform_monitor_check

router = APIRouter()

@router.post("/monitors/{monitor_id}/check", response_model= CheckResultResponse)
def check_monitor(
    monitor_id : int,
    db = Depends(get_db),
    current_user = Depends(get_current_user)
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
    
    check_result = perform_monitor_check(
    monitor,
    db
    )

    return check_result
    
@router.get("/monitors/{monitor_id}/results", response_model=list[CheckResultResponse])
def get_monitor_results(
    monitor_id : int,
    db = Depends(get_db),
    current_user = Depends(get_current_user)
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

    results = db.query(CheckResult).filter(
        CheckResult.monitor_id == monitor_id
    ).order_by(CheckResult.checked_at.desc()).all()

    return results