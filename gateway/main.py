from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':

        trend_response = requests.get("http://trend-predictor:5040/")

        json = trend_response.json()

        return jsonify({'data': json})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5050)