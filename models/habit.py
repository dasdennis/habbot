from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey # type: ignore
from sqlalchemy.sql import func # type: ignore
from models.base import Base

class Habit(Base):
  __tablename__ = "habits"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, nullable=False)
  name = Column(String(30), nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
  is_active = Column(Boolean, default=True)
