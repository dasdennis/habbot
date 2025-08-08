from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from sqlalchemy.exc import SQLAlchemyError
from db.database import SessionLocal
from models.habit import Habit

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  args = context.args

  if not args:
    await update.message.reply_text("Please provide a habit using /add <habit_name>.")
    return

  habit_name = " ".join(args)
  session = SessionLocal()

  try:
    new_habit = Habit(user_id=user_id, name=habit_name)
    session.add(new_habit)
    session.commit()
    await update.message.reply_text(f"Habit added successfully!")
  except SQLAlchemyError:
    session.rollback()
    await update.message.reply_text("An error occurred while adding the habit. Please try again.")
  finally:
    session.close()

add_handler = CommandHandler("add", add)
