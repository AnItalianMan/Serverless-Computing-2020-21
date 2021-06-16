from handlers import MqttHandler
from sensor_connectors import BluetoothManager

if __name__ == '__main__':
    mac = BluetoothManager.discover_devices("HC-05")
    if mac is None:
        raise ValueError("Device not found")
    exchange_name = "topic.sensors"
    routing_key = "*.*.photoresistor"
    queue_name = "sensor_values"

    sender = MqttHandler("admin", "serverlessistheway")
    sender.routing_key = routing_key
    sender.exchange_name = exchange_name
    sender.create_exchange(exchange_name, "topic")
    sender.create_queue(queue_name)
    sender.bind_queue(exchange_name, queue_name, routing_key)

    bluetooth_manager = BluetoothManager(mac, sender)
    bluetooth_manager.start()
    bluetooth_manager.receive_messages()
    print(BluetoothManager.discover_devices("HC-05"))