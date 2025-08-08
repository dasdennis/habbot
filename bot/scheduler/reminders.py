from telegram import Bot
from db.database import SessionLocal
from models.habit import Habit

async def send_daily_reminders(bot: Bot):
  session = SessionLocal()
  try:
    user_ids = session.query(Habit.user_id).distinct().all()
    for (user_id,) in user_ids:
      habits = session.query(Habit).filter_by(user_id=user_id, is_active=True).all()
      if habits:
        habit_list = "\n".join(f"* {h.name}" for h in habits)
        await bot.send_message(
          chat_id=user_id,
          text=f"⏰ Daily Habit Reminder:\n{habit_list}"
        )
  finally:
    session.close()
