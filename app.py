from flask import Flask
import sys, json, os, urllib, random
from config.twitter_client import getAPI

app = Flask(__name__)

GM_BOT_ID = os.getenv('bot_id')
twitterAPI = getAPI()


@app.route('/')
def recieveMessage():
    data = request.get_json()
    twitterAPI.update_status(data['text'])

