from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class IncidentResponse(BaseModel):
    id: int
    monitor_id: int
    checkresult_id: int
    message: str
    severity: str
    resolved: bool
    created_at: datetime
    resolved_at: Optional[datetime]


    class Config:
        from_attributes = True