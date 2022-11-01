import os
import logging
import vk_api
from vk_bot import echo
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from tg_bot import start, help_command, hello
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)


def main():
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')
    vk_token = os.getenv('VK_TOKEN')
    application = Application.builder().token(vk_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT, hello))
    application.run_polling()

    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk)


if __name__ == '__main__':
    main()
