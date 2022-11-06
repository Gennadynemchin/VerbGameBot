import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters
from dialogflow import detect_intent_texts


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.name}!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    user_id = update.message.from_user.id
    if text:
        answer, _ = detect_intent_texts(text, user_id)
        await update.message.reply_text(answer)


def main():
    logger = logging.getLogger(__name__)
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')

    application = Application.builder().token(tg_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, hello))
    application.run_polling()


if __name__ == '__main__':
    main()
