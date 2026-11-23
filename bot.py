import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8950995201:AAHA8hb7IIjIxA3NMDyJ_ylbKv5W5YbHF2E"

CODES_TEXT = """🇰🇪 SOSIOT - Daily Booking Codes

🔥 CODE 1: B88K-12345
   Odds: 15.2

🔥 CODE 2: B88K-67890
   Odds: 28.5

👉 How to use:
1. Go to betway.co.ke
2. Click Booking Code
3. Paste code

We are NOT Betway. We only share codes."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CODES_TEXT)

async def codes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CODES_TEXT)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("codes", codes))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
