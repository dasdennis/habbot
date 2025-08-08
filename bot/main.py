from telegram.ext import ApplicationBuilder # type: ignore
from bot.config import BOT_TOKEN
from bot.handlers import start_handler # type: ignore
from db.database import init_db
from bot.handlers.add import add_handler
from bot.handlers.list import list_handler
from bot.handlers.done import done_handler
from bot.handlers.stats import stats_handler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.scheduler.reminders import send_daily_reminders
from telegram import Bot

def main():
  init_db()  # Initialize the database
  application = ApplicationBuilder().token(BOT_TOKEN).build() # pyright: ignore[reportArgumentType]

  # Handlers
  application.add_handler(start_handler)
  application.add_handler(add_handler)
  application.add_handler(list_handler)
  application.add_handler(done_handler)
  application.add_handler(stats_handler)

  # Scheduler
  scheduler = AsyncIOScheduler(timezone="America/Sao_Paulo")
  scheduler.add_job(send_daily_reminders, "cron", hour=8, minute=0, args=[Bot(BOT_TOKEN)])
  scheduler.start()

  print("Bot is starting...")
  application.run_polling()

if __name__ == "__main__":
  main()
