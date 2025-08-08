# Telegram Habit Tracker Bot

A simple Telegram bot to track daily habits.
Built with **Python**, **python-telegram-bot**, **SQLAlchemy**, and **APScheduler**.

---

## 📌 Features
- `/start` — Register the user
- `/add <habit>` — Add a new habit
- `/list` — List active habits
- `/done <habit>` — Mark habit as completed today
- `/stats` — Show progress statistics for each habit
- Automatic daily reminders at 08:00 (configurable)

---

## 🛠 Requirements
- Python 3.11+
- Telegram Bot Token from [BotFather](https://core.telegram.org/bots#botfather)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/dasdennis/habbot.git
cd habbot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
