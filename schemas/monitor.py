from pydantic import BaseModel

class MonitorCreate(BaseModel):
    name : str
    url : str
    method : str
    check_interval : int
    latency_threshold : int
    timeout_seconds : int = 5

    