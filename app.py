from flask import Flask, request
import sys, json, os, urllib, random
from config.twitter_client import getAPI

app = Flask(__name__)

twitterAPI = getAPI()



@app.route('/')
def recieveMessage():
    data = request.get_json()
    print("**MESSAGE RECIEVED**")

    twitterAPI.update_status(data['text'])

    return("hello")
