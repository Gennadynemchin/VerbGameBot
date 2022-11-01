import os
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv


def vk_bot(token):
    vk_session = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('New message:')
            if event.to_me:
                print('Message from: ', event.user_id)
            else:
                print('My message for: ', event.user_id)
            print(f'Text: {event.text}\n')


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1, 1000)
    )


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk)


if __name__ == "__main__":
    main()


