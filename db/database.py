from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from bot.config import DB_PATH
from models.base import Base
from models.habit import Habit
from models.habit_check import HabitCheck

engine = create_engine("DB_PATH", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
  Base.metadata.create_all(bind=engine)
