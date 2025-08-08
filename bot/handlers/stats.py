from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from db.database import SessionLocal
from models.habit import Habit
from models.habit_check import HabitCheck
from datetime import date
from sqlalchemy import func

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  session = SessionLocal()

  try:
    habits = session.query(Habit).filter_by(user_id=user_id, is_active=True).all()
    if not habits:
      await update.message.reply_text("You have no active habits.")
      return

    response = "📊 Your Habit Stats:\n"

    for habit in habits:
      total_days = (date.today() - habit.created_at.date()).days + 1
      done_count = session.query(func.count()).select_from(HabitCheck).filter_by(habit_id=habit.id).scalar()
      percent = (done_count / total_days * 100) if total_days > 0 else 0
      response += f"• {habit.name}: {done_count}/{total_days} days ({percent:.1f}%)\n"
    await update.message.reply_text(response)
  finally:
    session.close()

stats_handler = CommandHandler("stats", stats)
