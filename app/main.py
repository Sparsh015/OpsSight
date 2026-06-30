from fastapi import FastAPI
from routers import check_result
from routers.auth import router
from routers.monitor import router as monitor_router
from routers.check_result import router as check_result
from app.scheduler import scheduler


app = FastAPI()
app.include_router(router)
app.include_router(monitor_router)
app.include_router(check_result)

@app.on_event("startup")
def start_scheduler():
    scheduler.start()