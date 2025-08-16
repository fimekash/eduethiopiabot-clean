import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, ContextTypes, filters
)

# --- CONFIG ---
BOT_TOKEN = "8399076842:AAFQ3M5gj4TmD9ZaeyIfqP9lWcxJPYl6fVo"
ADMIN_CHAT_ID = 6872304983
MAIN_CHANNEL = "https://t.me/eduethiopia"
YOUTUBE = "https://www.youtube.com/@eduethiopia"

# --- LOGGING ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- START MENU ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 Free Lessons", callback_data="free_lessons")],
        [InlineKeyboardButton("🎥 Video Lessons", url=YOUTUBE)],
        [InlineKeyboardButton("📝 Quizzes", callback_data="quizzes")],
        [InlineKeyboardButton("❓ Ask Question", url="https://t.me/eduethiopia_ask")],
        [InlineKeyboardButton("📄 Attractive Notes (Paid)", callback_data="notes")],
        [InlineKeyboardButton("💖 Teacher Support", callback_data="support")],
        [InlineKeyboardButton("📢 Main Channel", url=MAIN_CHANNEL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = (
        "🌍 Welcome to *Edu_pia Bot*!\n\n"
        "Your hub for world-class lessons in:\n"
        "📘 Mathematics, ⚗️ Chemistry, 🔬 Physics, 🧬 Biology, 💻 ICT, 📖 English\n\n"
        "👉 Choose an option below."
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

# --- FREE LESSONS MENU ---
async def free_lessons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Grade 9", url="https://t.me/eduethiopia_Grade9")],
        [InlineKeyboardButton("Grade 10", url="https://t.me/eduethiopia_Grade10")],
        [InlineKeyboardButton("Grade 11", url="https://t.me/eduethiopia_Grade11")],
        [InlineKeyboardButton("Grade 12", url="https://t.me/eduethiopia_Grade12")],
        [InlineKeyboardButton("⬅️ Back", callback_data="main")],
    ]
    await query.edit_message_text("📚 *Free Lessons* — Select your grade:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# --- QUIZZES ---
async def quizzes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Q1", callback_data="q1")],
        [InlineKeyboardButton("Q2", callback_data="q2")],
        [InlineKeyboardButton("Q3", callback_data="q3")],
        [InlineKeyboardButton("Q4", callback_data="q4")],
        [InlineKeyboardButton("Q5", callback_data="q5")],
        [InlineKeyboardButton("⬅️ Back", callback_data="main")],
    ]
    await query.edit_message_text("📝 *World-Class Quizzes* — Pick a question:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# --- QUIZ ANSWERS ---
async def quiz_answers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query.data
    answers = {
        "q1": "Q1: What is H₂O?\n✅ Answer: Water",
        "q2": "Q2: Which planet is called the Red Planet?\n✅ Answer: Mars",
        "q3": "Q3: Who is the father of modern physics?\n✅ Answer: Albert Einstein",
        "q4": "Q4: π (pi) is approximately?\n✅ Answer: 3.14159",
        "q5": "Q5: The powerhouse of the cell?\n✅ Answer: Mitochondria",
    }
    await update.callback_query.edit_message_text(answers[q])

# --- NOTES (PAID) ---
async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("💳 How to Pay", callback_data="support")],
        [InlineKeyboardButton("📝 Redeem Notes", callback_data="redeem_info")],
        [InlineKeyboardButton("⬅️ Back", callback_data="main")],
    ]
    await query.edit_message_text("📄 *Attractive Notes (Paid)*\n\nSupport teacher → Get PDF notes for Grades 9–12.", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# --- SUPPORT (PAYMENT) ---
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BOA", url="https://www.boa.com/yourpaymentlink")],
        [InlineKeyboardButton("CBE", url="https://www.cbe.com/yourpaymentlink")],
        [InlineKeyboardButton("Telebirr", url="https://www.telebirr.com/yourpaymentlink")],
        [InlineKeyboardButton("⬅️ Back", callback_data="main")],
    ]
    await query.edit_message_text("💖 Support your teacher via:", reply_markup=InlineKeyboardMarkup(keyboard))

# --- REDEEM NOTES ---
async def redeem_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    text = (
        "✅ *How to Redeem Notes*\n\n"
        "After payment, use this command:\n"
        "`/redeem METHOD TXID GRADE`\n\n"
        "Example:\n`/redeem Telebirr AB123456789 Grade11`\n\n"
        "Your request will be sent to admin. After confirmation, you’ll receive note links."
    )
    await query.edit_message_text(text, parse_mode="Markdown")

# --- /REDEEM HANDLER ---
async def redeem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage:\n/redeem METHOD TXID GRADE\nExample:\n/redeem Telebirr AB123456789 Grade11")
        return
    method, txid = args[0], args[1]
    grade = args[2] if len(args) >= 3 else "Not specified"
    msg = (
        f"📥 Redeem Request\n\n"
        f"👤 User: {user.full_name} (ID: {user.id})\n"
        f"💳 Method: {method}\n"
        f"🧾 TXID: {txid}\n"
        f"📘 Grade: {grade}"
    )
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)
    await update.message.reply_text("✅ Your redeem request was sent to admin. Please wait for confirmation.")

# --- PAYMENT PROOF (PHOTO/DOCS) ---
async def forward_proof(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.forward(chat_id=ADMIN_CHAT_ID)
    await update.message.reply_text("📤 Payment proof forwarded to admin.")

# --- CALLBACK HANDLER ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data == "main":
        await start(update, context)
    elif data == "free_lessons":
        await free_lessons(update, context)
    elif data == "quizzes":
        await quizzes(update, context)
    elif data in ["q1","q2","q3","q4","q5"]:
        await quiz_answers(update, context)
    elif data == "notes":
        await notes(update, context)
    elif data == "support":
        await support(update, context)
    elif data == "redeem_info":
        await redeem_info(update, context)

# --- MAIN ---
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("redeem", redeem))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.ALL, forward_proof))
    print("Edu_pia Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
