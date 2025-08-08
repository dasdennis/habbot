from SQLAlchemy import Column, Integer, Date, ForeignKey, UniqueConstraint # type: ignore
from models.base import Base
from datetime import date

class HabitCheck(Base):
  __tablename__ = "habit_checks"
  id = Column(Integer, primary_key=True)
  habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
  date = Column(Date, default=date.today)

  __table_args__ = (
    UniqueConstraint("habit_id", "date", name="uix_habit_date"),
  )
