import pika
from interfaces import HanderInterface


class MqttConsumer:

    def __init__(self, username: str, password: str, queue_name: str, handler: HanderInterface,
                 host: str = 'rabbitmq', port: int = 5672):
        credentials = pika.PlainCredentials(username, password)
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, credentials=credentials))
        self._channel = self._connection.channel()
        print("Channel created")
        self._queue_name = queue_name
        self._channel.queue_declare(queue=queue_name)
        print("Queue created")
        self._handler = handler

    def consume_messages(self):
        print("Consuming messages")
        for method_frame, properties, body in self._channel.consume(self._queue_name, auto_ack=True):
            self._handler.handle(body)