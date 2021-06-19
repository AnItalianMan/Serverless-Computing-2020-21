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
        self._sock.send("OK")

    def receive_messages(self):
        if self._sock is None:
            print("The socket is not started yed")
            return

        print("Starting the listener")
        msg = ""
        while True:
            data = self._sock.recv(1)
            data = data.decode("UTF-8")
            if data == "\n":
                self._handler.handle(msg)
                msg = ""
            else:
                msg += data

