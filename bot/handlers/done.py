from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from db.database import SessionLocal
from models.habit import Habit
from models.habit_check import HabitCheck
from sqlalchemy.exc import IntegrityError

async def mark_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_id = update.effective_user.id
  args = context.args

  if not args:
    await update.message.reply_text("Use: /done <habit_id>")
    return

  habit_name = " ".join(args)
  session = SessionLocal()

  try:
    habit = session.query(Habit).filter_by(user_id=user_id, name=habit_name, is_active=True).first()
    if not habit:
      await update.message.reply_text("Habit not found!")
      return

    check = HabitCheck(habit_id=habit.id)
    session.add(check)
    session.commit()
    await update.message.reply_text(f"Habit '{habit_name}' has been marked as completed for today!")
  except IntegrityError:
    session.rollback()
    await update.message.reply_text("Habit already updated today!")
  finally:
    session.close()

done_handler = CommandHandler("done", mark_done)
