from apscheduler.schedulers.background import BackgroundScheduler

from app.database import SessionLocal
from models import Monitor
from services.monitor_service import perform_monitor_check

scheduler = BackgroundScheduler()

def check_all_monitors():
    db = SessionLocal()
    try:
        monitors = db.query(Monitor).filter(
            Monitor.is_active == True
        ).all()

        for monitor in monitors:
            print(monitor.name)
            perform_monitor_check(monitor, db)
    finally:
        db.close()
    
scheduler.add_job(
    check_all_monitors,
    "interval",
    seconds = 10
)
