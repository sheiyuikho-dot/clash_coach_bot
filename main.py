from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("8436353722:AAFWu1NLSo2XkQEwfiKplyDQbydVkxR6IQQ")

def get_upgrade_suggestion(th, lab, king, queen):
    suggestions = []
    if lab < (th + 2):
        suggestions.append("Upgrade your Laboratory first.")
    if king < (th * 2):
        suggestions.append("Upgrade your Barbarian King.")
    if queen < (th * 2):
        suggestions.append("Upgrade your Archer Queen.")
    if not suggestions:
        suggestions.append("Your base is well balanced! Focus on walls and traps.")
    return "\n".join(suggestions)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Clash Coach Bot 🛡\n"
        "Send your base info like:\nTH=10 Lab=7 King=15 Queen=14"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        parts = text.lower().replace("=", " ").split()
        th = int(parts[1])
        lab = int(parts[3])
        king = int(parts[5])
        queen = int(parts[7])
        suggestion = get_upgrade_suggestion(th, lab, king, queen)
        await update.message.reply_text(f"🏰 Upgrade Suggestions:\n{suggestion}")
    except:
        await update.message.reply_text("⚠ Wrong format. Example: TH=10 Lab=7 King=15 Queen=14")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
