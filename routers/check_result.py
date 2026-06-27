from fastapi import APIRouter, Depends, HTTPException
from models import Monitor, CheckResult
from auth.token import get_current_user
from app.database import get_db
import httpx
import time
from schemas.check_result import CheckResultResponse

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
    
    try:
        start_time = time.time()
        response = httpx.request(
        method=monitor.method,
        url=monitor.url,
        timeout=monitor.timeout_seconds,
        follow_redirects=True
    )

        end_time = time.time()
        response_time = int((end_time - start_time) * 1000)

        check_result = CheckResult(
            monitor_id = monitor.id,
            status_code = response.status_code,
            response_time = response_time,
            is_success = response.is_success,
            error_desc = None if response.is_success else response.reason_phrase
        )
    
    except Exception as e:
        check_result = CheckResult(
            monitor_id = monitor.id,
            status_code = None,
            response_time = None,
            is_success = False,
            error_desc = str(e)
        )

    db.add(check_result)
    db.commit()
    db.refresh(check_result)

    return check_result


