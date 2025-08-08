from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")

BOT_NAME = os.getenv("BOT_NAME", "Habbot")
if not BOT_NAME:
    raise ValueError("BOT_NAME is not set in the environment variables.")

DB_PATH = os.getenv("DB_PATH")
if not DB_PATH:
    raise ValueError("DB_PATH is not set in the environment variables.")
