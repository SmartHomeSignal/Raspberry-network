import websocket
import threading


class Network(object):

    def __init__(self):
        super().__init__()
        self._websocket = None
        self._receive_callback = None

    def connect(self, receive_callback):
        self._receive_callback = receive_callback

        def _on_message(ws, message):
            print("[Network] received: {}".format(message))
            receive_callback(message)

        self._websocket = websocket.WebSocketApp(
            "ws://45.15.253.128:8090/clients/signal",
            on_message=_on_message,
            on_error=self._on_error,
            on_close=self._on_close,
            on_open=self._on_open
        )

        thread = threading.Thread(target=self._run, args=())
        thread.start()

    def enable_signal(self):
        print("[Network] sending 'true' to socket")
        self._websocket.send("true")

    def disable_signal(self):
        print("[Network] sending 'false' to socket")
        self._websocket.send("false")

    def disconnect(self):
        self._websocket.close()

    def _run(self):
        self._websocket.run_forever()

    @staticmethod
    def _on_error(ws, error):
        print("[Network] error: {}".format(error))

    @staticmethod
    def _on_close(ws):
        print("[Network] connection closed")

    @staticmethod
    def _on_open(ws):
        print("[Network] connected to socket")
