from consumers import MqttConsumer
from handlers import TelegramHandler
import os

if __name__ == '__main__':
    handler = TelegramHandler(os.environ['BOT_TOKEN'], os.environ['CHAT_ID'])
    consumer = MqttConsumer(os.environ['USERNAME'], os.environ['PASSWORD'], os.environ['QUEUE_NAME'], handler)
    consumer.consume_messages()
