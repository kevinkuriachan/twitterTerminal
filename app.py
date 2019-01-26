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
    print("**MESSAGE RECIEVED**")

    twitterAPI.update_status(data['text'])

    return "ok", 200
