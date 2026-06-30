from datetime import datetime

from models import Incident


def handle_incident(
    monitor,
    check_result,
    db
):
    is_healthy = (
        check_result.is_success
        and check_result.response_time <= monitor.latency_threshold
    )

    existing_incident = db.query(Incident).filter(
        Incident.monitor_id == monitor.id,
        Incident.resolved == False
    ).first()

    # -------------------------
    # Website is healthy
    # -------------------------
    if is_healthy:

        if existing_incident:
            existing_incident.resolved = True
            existing_incident.resolved_at = datetime.now()
            db.commit()

        return

    # -------------------------
    # Website is unhealthy
    # -------------------------

    # Don't create duplicate incidents
    if existing_incident:
        return

    # Decide incident message & severity
    if (
        check_result.response_time is not None
        and check_result.response_time > monitor.latency_threshold
    ):

        message = (
            f"Latency threshold exceeded ({check_result.response_time} ms)"
        )
        severity = "Medium"

    else:

        message = (
            check_result.error_desc
            or f"Website returned status code {check_result.status_code}"
        )
        severity = "High"

    incident = Incident(
        monitor_id=monitor.id,
        checkresult_id=check_result.id,
        message=message,
        severity=severity
    )

    db.add(incident)
    db.commit()