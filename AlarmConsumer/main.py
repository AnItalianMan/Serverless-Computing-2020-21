from consumers import MqttConsumer
from handlers import TelegramHandler

if __name__ == '__main__':
    handler = TelegramHandler("BOT_TOKEN", "CHAT_ID")
    consumer = MqttConsumer("administrator", "serverlessistheway", "alarm", handler)
    consumer.consume_messages()
