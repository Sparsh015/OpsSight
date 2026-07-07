from fastapi import FastAPI
from routers import check_result
from routers.auth import router
from routers.monitor import router as monitor_router
from routers.check_result import router as check_result
from app.scheduler import scheduler
from routers.incident import router as incident_router

app = FastAPI()
app.include_router(router)
app.include_router(monitor_router)
app.include_router(check_result)
app.include_router(incident_router)

@app.on_event("startup")
def start_scheduler():
    print("starting scheduler")
    scheduler.start()

@app.on_event("shutdown")
def stop_scheduler():

    scheduler.shutdown()

@app.get("/")
def home():
    return {
        "message": "OpsSight API Monitoring System",
        "docs": "/docs"
    }