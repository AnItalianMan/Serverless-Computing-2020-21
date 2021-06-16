from interfaces import HanderInterface
import time
import bluetooth


class BluetoothManager:

    def __init__(self, mac: str, handler: HanderInterface, port: int = 1):
        self._mac = mac
        self._port = port
        self._sock = None
        self._handler = handler

    @staticmethod
    def discover_devices(target):
        devices = bluetooth.discover_devices(duration=20, lookup_names=True)
        for device_mac, device_name in devices:
            if device_name == target:
                return device_mac
        return None

    def start(self):
        self._sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self._sock.connect((self._mac, self._port))
        print("Connection to bluetooth device created")

    def receive_messages(self):
        if self._sock is None:
            print("The socket is not started yed")
            return

        print("Starting the listener")
        self._sock.recv(4096)
        while True:
            data = self._sock.recv(3)
            self._handler.handle(data)
            time.sleep(0.01)
