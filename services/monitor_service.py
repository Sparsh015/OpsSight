import time
import httpx
from datetime import datetime

from models import CheckResult
from services.incident_service import handle_incident
from app.logger import logger


def perform_monitor_check(
    monitor,
    db
):
    logger.info(
        f"Starting check for monitor: {monitor.name}"
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

        response_time = int(
            (end_time - start_time) * 1000
        )


        logger.info(
            f"{monitor.name} returned {response.status_code} "
            f"in {response_time} ms"
        )


        check_result = CheckResult(
            monitor_id=monitor.id,
            status_code=response.status_code,
            response_time=response_time,
            is_success=response.is_success,
            error_desc=None if response.is_success else response.reason_phrase
        )


    except Exception as e:

        logger.error(
            f"{monitor.name} check failed: {str(e)}"
        )
        check_result = CheckResult(
            monitor_id=monitor.id,
            status_code=None,
            response_time=None,
            is_success=False,
            error_desc=str(e)
        )

    db.add(check_result)

    monitor.last_checked = datetime.now()
    db.commit()
    db.refresh(check_result)

    handle_incident(
        monitor,
        check_result,
        db
    )
    return check_result