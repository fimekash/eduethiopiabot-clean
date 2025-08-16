import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- CONFIG ---
BOT_TOKEN = "8399076842:AAFQ3M5gj4TmD9ZaeyIfqP9lWcxJPYl6fVo"
ADMIN_CHAT_ID = 6872304983  # Your Telegram ID

# --- LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- START MENU ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Grade 9", callback_data="grade9")],
        [InlineKeyboardButton("Grade 11", callback_data="grade11")],
        [InlineKeyboardButton("Grade 12", callback_data="grade12")],
        [InlineKeyboardButton("Teacher Support ❤️", callback_data="support")],
        [InlineKeyboardButton("Quizzes", callback_data="quizzes")],
        [InlineKeyboardButton("Ask Question", callback_data="ask")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to Edu_pia! Choose an option below:", reply_markup=reply_markup)

# --- BUTTON HANDLER ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --- Grade 9 ---
    if query.data == "grade9":
        text = """
📘 *Grade 9 Courses*

1. Mathematics ➝ [Click here](https://t.me/eduethiopia_Grade9_Math)
2. Physics ➝ [Click here](https://t.me/eduethiopia_Grade9_Physics)
3. Chemistry ➝ [Click here](https://t.me/eduethiopia_Grade9_Chemistry)
4. Biology ➝ [Click here](https://t.me/eduethiopia_Grade9_Biology)
5. English ➝ [Click here](https://t.me/eduethiopia_Grade9_English)
        """
        await query.edit_message_text(text, parse_mode="Markdown")

    # --- Grade 11 ---
    elif query.data == "grade11":
        text = """
📘 *Grade 11 Courses*

1. Mathematics ➝ [Click here](https://t.me/eduethiopia_Grade11_Math)
2. Physics ➝ [Click here](https://t.me/eduethiopia_Grade11_Physics)
3. Chemistry ➝ [Click here](https://t.me/eduethiopia_Grade11_Chemistry)
4. Biology ➝ [Click here](https://t.me/eduethiopia_Grade11_Biology)
5. English ➝ [Click here](https://t.me/eduethiopia_Grade11_English)
        """
        await query.edit_message_text(text, parse_mode="Markdown")

    # --- Grade 12 ---
    elif query.data == "grade12":
        text = """
📘 *Grade 12 Courses*

1. Mathematics ➝ [Click here](https://t.me/eduethiopia_Grade12_Math)
2. Physics ➝ [Click here](https://t.me/eduethiopia_Grade12_Physics)
3. Chemistry ➝ [Click here](https://t.me/eduethiopia_Grade12_Chemistry)
4. Biology ➝ [Click here](https://t.me/eduethiopia_Grade12_Biology)
5. English ➝ [Click here](https://t.me/eduethiopia_Grade12_English)
        """
        await query.edit_message_text(text, parse_mode="Markdown")

    # --- Teacher Support ❤️ ---
    elif query.data == "support":
        keyboard = [
            [InlineKeyboardButton("BOA", url="https://www.boa.com/yourpaymentlink")],
            [InlineKeyboardButton("CBE", url="https://www.cbe.com/yourpaymentlink")],
            [InlineKeyboardButton("Telebirr", url="https://www.telebirr.com/yourpaymentlink")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("💖 Support your teacher easily. Choose a payment method:", reply_markup=reply_markup)

    # --- Quizzes ---
    elif query.data == "quizzes":
        keyboard = [
            [InlineKeyboardButton("Q1", callback_data="q1")],
            [InlineKeyboardButton("Q2", callback_data="q2")],
            [InlineKeyboardButton("Q3", callback_data="q3")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📝 *World-Class STEM Quizzes*\nChoose a question:", reply_markup=reply_markup, parse_mode="Markdown")

    # --- Ask Question ---
    elif query.data == "ask":
        text = "❓ *Ask a Question*\n\nAsk your question here:\n[t.me/eduethiopia_ask](https://t.me/eduethiopia_ask)"
        await query.edit_message_text(text, parse_mode="Markdown")

    # --- Quiz Answers ---
    elif query.data == "q1":
        text = "Q1: What is the chemical symbol for water?\n✅ Answer: H₂O"
        await query.edit_message_text(text)

    elif query.data == "q2":
        text = "Q2: What planet is known as the Red Planet?\n✅ Answer: Mars"
        await query.edit_message_text(text)

    elif query.data == "q3":
        text = "Q3: Who is known as the father of modern physics?\n✅ Answer: Albert Einstein"
        await query.edit_message_text(text)

# --- MAIN FUNCTION ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("Edu_pia Bot is running...")
    app.run_polling()