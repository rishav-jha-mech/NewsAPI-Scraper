import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def home():
    url = 'https://newsapi.org/v2/everything?q=' + request.args.get('coin') + f'&apiKey={API_KEY}'
    res = requests.get(url)
    return res.json()