import datetime
from flask import Flask, jsonify
from orm.Model import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    raw = get_trading_data()

    moving_average = calculate_moving_average(raw)

    return jsonify({'moving_average': moving_average})


def get_trading_data():
    query = (Trade.
             select(Trade.time, Trade.price).
             where(Trade.symbol == "BINANCE:BTCUSDT").
             where(Trade.time > datetime.datetime.now() - datetime.timedelta(seconds=5)).
             order_by(Trade.time.asc()))
    results = query.execute()
    return results


def calculate_moving_average(results):
    moving_window_length = 5
    moving_average = []
    for i in range(moving_window_length, len(results)):
        s = 0

        for w in range(0, moving_window_length):
            p = results[i - w - 1].price
            s += p

        avg = s / moving_window_length
        moving_average.append(avg)

    return moving_average


if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5040)