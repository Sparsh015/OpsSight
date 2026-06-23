from fastapi import FastAPI
from routers.auth import router
from routers.monitor import router as monitor_router

app = FastAPI()
app.include_router(router)
app.include_router(monitor_router)