import os
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
            print('Text:', event.text)


load_dotenv()
vk_bot(os.getenv('VK_TOKEN'))
