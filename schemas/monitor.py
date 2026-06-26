from pydantic import BaseModel

class MonitorCreate(BaseModel):
    name : str
    url : str
    method : str
    check_interval : int
    latency_threshold : int
    timeout_seconds : int = 5

class MonitorResponse(BaseModel):
    id: int
    user_id: int
    name: str
    url: str
    method: str
    check_interval: int
    latency_threshold: int
    timeout_seconds: int
    is_active: bool

    class Config: 
        from_attributes = True

class MonitorUpdate(BaseModel):
    name: str
    url = str
    method: str
    check_interval: int
    latency_threshold: int
    timeout_seconds: int
    is_active: bool