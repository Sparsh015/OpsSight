from apscheduler.schedulers.background import BackgroundScheduler

from app.database import SessionLocal
from models import Monitor
from services.monitor_service import perform_monitor_check
from datetime import timedelta, datetime
from app.logger import logger

scheduler = BackgroundScheduler()

def check_all_monitors():
    logger.info("Running scheduled monitor checks")
    db = SessionLocal()
    try:
        monitors = db.query(Monitor).filter(
            Monitor.is_active == True
        ).all()

        for monitor in monitors:

            if monitor.last_checked is None:
                perform_monitor_check(monitor, db)
                continue

            next_check_time = (
                monitor.last_checked + timedelta(seconds=monitor.check_interval)
            )
            if datetime.now() >= next_check_time:
                perform_monitor_check(monitor, db)

    finally:
        db.close()
    
scheduler.add_job(
    check_all_monitors,
    "interval",
    seconds = 10,
    max_instances = 3
)
