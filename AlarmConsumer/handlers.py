import requests
from interfaces import HanderInterface


class TelegramHandler(HanderInterface):
    def __init__(self, bot_token, bot_chat_id):
        self._bot_chat_id = bot_chat_id
        self._bot_token = bot_token

    def handle(self, data):
        send_text = 'https://api.telegram.org/bot' + self._bot_token + '/sendMessage?chat_id=' + self._bot_chat_id + '&parse_mode=Markdown&text=' + data
        requests.get(send_text)
