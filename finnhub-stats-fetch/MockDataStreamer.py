from time import sleep
from typing import override
from DataStreamerBase import *

class MockDataStreamer(DataStreamerBase):

    __mockMessage = """{
  "data": [
    {
      "p": 10.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691134,
      "v": 0.011467
    },
    {
      "p": 15.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691234,
      "v": 0.011467
    },
    {
      "p": 20.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691334,
      "v": 0.011467
    },
    {
      "p": 25.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691434,
      "v": 0.011467
    },
    {
      "p": 30.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691534,
      "v": 0.011467
    },
    {
      "p": 25.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691634,
      "v": 0.011467
    },
    {
      "p": 10.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691734,
      "v": 0.011467
    },
    {
      "p": 10.00,
      "s": "BINANCE:BTCUSDT",
      "t": 1575526691834,
      "v": 0.011467
    }
  ],
  "type": "trade"
}"""

    def __init__(self, callback):
        DataStreamerBase.__init__(self, callback)

    @override
    def start(self) -> None:
        super(MockDataStreamer, self).start()
        sleep(1)
        self.callback(self.__mockMessage)
