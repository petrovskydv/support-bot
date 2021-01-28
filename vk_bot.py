import os
import random

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from utils import detect_intent_texts


def echo(event, vk_api, answer):
    vk_api.messages.send(
        user_id=event.user_id,
        message=answer,
        random_id=random.randint(1, 1000)
    )


def main():
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    project_id = os.environ['GOOGLE_PROJECT_ID']
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer = detect_intent_texts(project_id, event.user_id, [event.text], 'ru')
            echo(event, vk_api, answer)


if __name__ == "__main__":
    main()
