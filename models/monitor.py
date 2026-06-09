from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

class Monitor(Base):
    __tablename__ = "monitors"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable = False)
    url = Column(String(500), nullable = False)
    method = Column(String(10), nullable=False)
    check_interval = Column(Integer, nullable = False)
    latency_threshold = Column(Integer, nullable = False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    last_checked = Column(DateTime, nullable=True)
    timeout_seconds = Column(Integer, default=5, nullable=False)

    user = relationship("User", back_populates="monitors")
    check_results = relationship("CheckResult",back_populates="monitor")
    incidents = relationship("Incident",back_populates="monitor")