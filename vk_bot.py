import os
import logging
import random
import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow import detect_intent_texts


def echo(event, vk_api, answer):
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer,
        random_id=random.randint(1, 1000)
    )


def main():
    logger = logging.getLogger(__name__)
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')

    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer, no_answer = detect_intent_texts(event.message, event.user_id)
            if not no_answer:
                echo(event, vk, answer)


if __name__ == '__main__':
    main()
