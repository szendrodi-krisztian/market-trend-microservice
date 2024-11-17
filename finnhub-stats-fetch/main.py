import datetime
import json

from FinnhubDataStreamer import *
from MockDataStreamer import *

from orm.Model import *

DataStreamer = FinnhubDataStreamer
#DataStreamer = MockDataStreamer

def on_data_incoming(data):
    parsed = json.loads(data)
    if parsed["type"] == "trade":

        delete_too_old_data()

        trade_array = parsed["data"]
        for single_trade in trade_array:
            Trade.create(price=single_trade["p"], symbol=single_trade["s"], time=datetime.datetime.fromtimestamp(single_trade["t"] / 1e3), volume=single_trade["v"])

def delete_too_old_data():
    Trade.delete().where(Trade.time < datetime.datetime.now() - datetime.timedelta(seconds=10)).execute()

if __name__ == '__main__':
    print("Connecting to database...")
    connect_to_database()

    print("Creating data fetcher...")
    fetcher = DataStreamer(on_data_incoming)

    print("Starting fetching...")
    fetcher.start()