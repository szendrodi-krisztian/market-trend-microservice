import os
import websocket
import finnhub
from typing import override
from pathlib import Path
from DataStreamerBase import *

class FinnhubDataStreamer(DataStreamerBase):
    __websocket = None

    def __init__(self, callback):
        super(FinnhubDataStreamer, self).__init__(callback)
        #websocket.enableTrace(True)
        self.__websocket = websocket.WebSocketApp("wss://ws.finnhub.io?token=" + FinnhubDataStreamer.get_finnhub_api_key(),
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.__websocket.on_open = self.on_open

    @override
    def start(self) -> None:
        super(FinnhubDataStreamer, self).start()
        self.__websocket.run_forever()

    def on_message(self, ws, message):
        self.callback(message)
        return

    def on_error(self, ws, error):
        print(f"Websocket error: {error}")
        return

    def on_close(self, ws, status_code, close_message):
        print(f"Closing websocket message: {close_message}")
        return

    def on_open(self, ws):
        print("Websocket opened")
        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
        return

    @staticmethod
    def get_finnhub_api_key():
        api_key_path = os.environ.get('FINNHUB_API_KEY')
        api_key_value = Path(api_key_path).read_text()
        return api_key_value

    @staticmethod
    def get_connection_to_finnhub() -> finnhub.Client:
        finnhub_client = finnhub.Client(api_key=FinnhubDataStreamer.get_finnhub_api_key())
        return finnhub_client
