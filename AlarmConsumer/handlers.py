import time

import requests
from interfaces import HanderInterface


class TelegramHandler(HanderInterface):
    def __init__(self, bot_token, bot_chat_id):
        self.__bot_chat_id = bot_chat_id
        self.__bot_token = bot_token
        self.__last_notification = time.time()

    def handle(self, data):
        current_time = time.time()
        if current_time - self.__last_notification > 15:
            send_text = 'https://api.telegram.org/bot' + self.__bot_token + '/sendMessage?chat_id=' + self.__bot_chat_id + '&parse_mode=Markdown&text=' + data.decode(
                "UTF-8")
            requests.get(send_text)
            self.__last_notification = current_time
