import vk_api, random, main
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime

token = '9747417985bcb99c0260f4a9baade9621a268aea5e8ad71851e5c7586bcd55d7a8ca55e142b38205d5c6d'
'''login = input('Enter your login>>>')
password = input('Enter your password>>>')

def auth_handler():
    key = input('Enter your key>>>')
    remember_device = True
    return key, remember_device


vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)'''

vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f'Message time is  {datetime.strftime(datetime.now(), "%H:%M:%S")}')
            print(f'Message text : {event.text}')
            response = event.text.lower()
            if event.from_user and not event.from_me:
                response_for_user = main.send_message(event.text)
                vk_session.method('messages.send', {
                    'user_id': event.user_id,
                    'message': response_for_user,
                    'random_id': random.randint(0, 2000000)
                })

