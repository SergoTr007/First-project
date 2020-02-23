from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = "4498f340fa807322a5a5b92301f87a88edc0c5711838f9cdda64c09fc8aa9dc96944d43c2b181cea9894c"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "лиходей":
                vk_session.method('messages.send',
                                  {'user_id': event.user_id, 'message': 'вот так вот', 'random_id': 0})