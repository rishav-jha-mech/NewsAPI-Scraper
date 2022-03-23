import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from flask_caching import Cache

load_dotenv()
API_KEY = os.getenv('API_KEY')
config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def home():
    coin = request.args.get('coin')
    
    if cache.get(coin) is None:
        print('Coin was not in cache and is sent to NewsApi server')
        url = f'https://newsapi.org/v2/everything?q={coin}&apiKey={API_KEY}'
        res = requests.get(url)
        cache.set(f'{coin}',res)
        return res.json()
    else:
        print('Coin was present in cache, and this is from there')
        res = cache.get(coin)
        return res.json()