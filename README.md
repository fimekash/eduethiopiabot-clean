# EduEthiopia Bot

Simple Telegram bot using python-telegram-bot, deployed on Render as a Background Worker (long polling).

## Local testing (optional)
- Create a file named .env with BOT_TOKEN=your_token (do NOT commit .env)
- Run: python bot.py

## Deploy on Render
- Build command: pip install -r requirements.txt
- Start command: python bot.py
- Environment Variable: BOT_TOKEN = (your token from BotFather)
