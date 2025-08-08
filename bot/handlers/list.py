from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from db.database import SessionLocal
from models.habit import Habit

async def list_habits(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  session = SessionLocal()

  try:
    habits = session.query(Habit).filter_by(user_id, is_active=True).all()
    if not habits:
      await update.message.reply_text("You have no active habits.")
      return

    response = "Your active habits:\n"
    for habit in habits:
      response += f"- {habit.name}\n"

      await update.message.reply_text(response)
  finally:
    session.close()

list_handler = CommandHandler("list", list_habits)
