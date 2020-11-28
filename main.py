from flask import Flask
from flask_cors import CORS
from config import prod_api_key, test_api_key
import requests
import json
app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "CryptoCurrency Data API"


@app.route('/api/market-data', methods=['GET'])
def get_coin_data():
    error = None
    #url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' #Prod API URL
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': test_api_key
    }

    try:
        r = requests.get(url, params=parameters, headers=headers)
        return json.dumps(r.text)
    except () as e:
        print(e)