from telegram import Update # type: ignore
from telegram.ext import CommandHandler, ContextTypes # type: ignore

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("👋 Hi! I'm your Healthy Habits Bot! Let's build great habits!")

start_handler = CommandHandler("start", start)
