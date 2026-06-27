from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CheckResultResponse(BaseModel):
    id: int
    monitor_id: int
    status_code: Optional[int]
    response_time: Optional[int]
    is_success: bool
    error_desc: Optional[str]
    checked_at: datetime

    class Config:
        from_attributes = True