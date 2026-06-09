from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

class CheckResult(Base):
    __tablename__ = "checkresults"
    id = Column(Integer, primary_key=True)
    monitor_id = Column(Integer, ForeignKey("monitors.id"), nullable=False)
    status_code = Column(Integer, nullable= True)
    response_time = Column(Integer, nullable= True)
    is_success = Column(Boolean, default = True)
    error_desc = Column(String(300), nullable = True)
    checked_at = Column(DateTime, default=datetime.now, nullable=False)

    monitor = relationship("Monitor", back_populates="checkresults")