from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from datetime import datetime

class Monitor(Base):
    __tablename__ = "monitors"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable = False)
    url = Column(String(500), nullable = False)
    method = Column(String(10), choices = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"], nullable = False)
    check_interval = Column(Integer, nullable = False)
    latency_threshold = Column(Integer, nullable = False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    last_checked = Column(DateTime, nullable=True)
    timeout_seconds = Column(Integer, default=5, nullable=False)
    