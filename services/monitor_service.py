import time
import httpx
from models import CheckResult

def perform_monitor_check(
    monitor,
    db
):
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