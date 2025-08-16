import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# --- CONFIG ---
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set this on Render → Environment → BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

WELCOME_TEXT = (
    "👋 Welcome to EduEthiopia Bot!\n"
    "Use the menu below or type /help."
)

HELP_TEXT = (
    "Commands:\n"
    "/start – start the bot\n"
    "/help – show this help\n"
)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("Grade 9", callback_data="grade9"),
         InlineKeyboardButton("Grade 10", callback_data="grade10")],
        [InlineKeyboardButton("Support", callback_data="support")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message(WELCOME_TEXT, reply_markup=main_menu())

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_chat.send_message(HELP_TEXT)

async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "support":
        await query.edit_message_text("Contact @YourUsername for support.")
    elif data == "grade9":
        await query.edit_message_text("Coming soon: Grade 9 resources.")
    elif data == "grade10":
        await query.edit_message_text("Coming soon: Grade 10 resources.")
    else:
        await query.edit_message_text("Unknown selection.")

async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Replies to any non-command text message
    await update.message.reply_text("I received your message 🙌")

def build_app():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN env var is missing.")
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CallbackQueryHandler(on_button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_text))

    return application

if __name__ == "__main__":
    app = build_app()
    # Long polling (simple + reliable). No webhook needed.
    app.run_polling(allowed_updates=Update.ALL_TYPES)
