from flask import Flask, request
import sys, json, os, urllib, random
from config.twitter_client import getAPI

app = Flask(__name__)

twitterAPI = getAPI()


@app.route('/')
def home():
    return "hello"

@app.route('/recieve', methods=['POST'])
def recieveMessage():
    data = request.get_json()

    if ("@bot#tweet: " in data['text']):
        stringToTweet = data['text'].replace("@bot#tweet: ", "")
        twitterAPI.update_status(stringToTweet)
    

    return "ok", 200
