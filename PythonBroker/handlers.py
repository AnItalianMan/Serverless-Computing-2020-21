from interfaces import HanderInterface
import pika


class MqttHandler(HanderInterface):

    def __init__(self, username: str, password: str, exchange: str = None, routing_key: str = None,
                 host: str = 'localhost', port: int = 5672):
        credentials = pika.PlainCredentials(username, password)
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, credentials=credentials))
        self._channel = self._connection.channel()
        self._exchange_name = exchange
        self._routing_key = routing_key

    @property
    def exchange_name(self):
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, value: str):
        self._exchange_name = value

    @property
    def routing_key(self):
        return self._routing_key

    @routing_key.setter
    def routing_key(self, value: str):
        self._routing_key = value

    def handle(self, data):
        if self._exchange_name is None or self._routing_key is None:
            raise ValueError("Exchange or routing key is None!")
        self.send(self._exchange_name, self._routing_key, data)

    def send(self, exchange: str, routing_key: str, message):
        self._channel.basic_publish(exchange=exchange,
                                    routing_key=routing_key,
                                    body=message)

    def create_exchange(self, exchange_name: str, exchange_type: str):
        self._channel.exchange_declare(exchange=exchange_name,
                                       exchange_type=exchange_type)
        print("Exchange created")

    def create_queue(self, queue_name: str):
        self._channel.queue_declare(queue=queue_name)
        print("Queue created")

    def bind_queue(self, exchange_name: str, queue_name: str, routing_key: str):
        self._channel.queue_bind(exchange=exchange_name,
                                 queue=queue_name, routing_key=routing_key)
        print("Queue binded")
