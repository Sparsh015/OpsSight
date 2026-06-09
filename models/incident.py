from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from app.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)
    monitor_id = Column(Integer, ForeignKey("monitors.id"), nullable = False)
    checkresult_id = Column(Integer, ForeignKey("checkresults.id"), nullable = False)
    message = Column(String(500), nullable = False)
    severity = Column(String(15), nullable=False)
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    resolved_at = Column(DateTime)
