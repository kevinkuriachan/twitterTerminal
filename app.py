from flask import Flask
import sys, json, os, urllib, random
from config.twitter_client import getAPI

app = Flask(__name__)

GM_BOT_ID = os.getenv('bot_id')

@app.route('/')
def recieveMessage():
    data = request.get_json()
    print(data['text'])

    return 'Hello, World!'

