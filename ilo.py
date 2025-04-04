import logging
import random
import pytz
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# --- Bot Token ---
BOT_TOKEN = "8155632460:AAH_wVS3P0vaNZIEsDaNbHxU3_HYTv4ZkT4"  # <<< Replace this with your actual bot token

# --- Logging ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Quotes & Images ---
birthday_quotes = [
    "Happy Birthday Sharmi 💞 you are the  love of my life! You make every day brighter with your ☺️smile.",
    "Your birthday is a gentle reminder of how lucky I am to have you. 💘Love you forever Sharmi 💕!",
    "Wishing you endless happiness, my queen 👑. You deserve all the love in the world!",
    "You are my sunshine, my joy, and my heart. Happy birthday, baby!",
    "On your special day, I just want you to know how deeply you’re loved. Happy Birthday Sweetheart 😘!"
]

birthday_images = [
    "love1.jpg",
    "love2.jpg",
    "love3.jpg",
    "love4.jpg",
    "love5.jpg"
]

# --- Message Sender ---
async def send_birthday_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = random.choice(birthday_quotes)
    image = random.choice(birthday_images)

    keyboard = [[InlineKeyboardButton(" Sharmi Tap Here 💖", callback_data='send_more')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=image,
        caption=f"**{quote}**\n\nWith all my love, only for you.",
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

# --- /start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey SHARMI 😍! Here's a special surprise for your Birthday 🎂:")
    await send_birthday_message(update, context)

# --- Button Handler ---
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await send_birthday_message(update, context)

# --- Main Bot Runner ---
def main():
    async def configure_scheduler(app):
        app.job_queue.scheduler.configure(timezone=pytz.utc)

    app = Application.builder().token(BOT_TOKEN).post_init(configure_scheduler).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Birthday bot is now running...")
    app.run_polling()

# --- Entry Point ---
if __name__ == '__main__':
    main()
