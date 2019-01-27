from flask import Flask, request
import sys, json, os, urllib, random
from config.twitter_client import getAPI
import praw, random, requests

app = Flask(__name__)

twitterAPI = getAPI()
redditAPI = reddit = praw.Reddit(client_id = os.getenv('redditID'), client_secret = os.getenv('redditSecret'), user_agent = 'my user agent')

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

    if ("@bot#pic: cat" in data['text']):
        sub = data['text'].replace("@bot#pic: ", "")
        print("SUBREDDIT: " + sub)
        submissions = list(redditAPI.subreddit('cat').hot(limit=150))
        size = len(submissions)
        url = submissions[random.randint(0,size)].url
        req = requests.get(url)
        with open('imgToTweet.jpg', 'wb') as openFile:
            openFile.write(req.content)
        twitterAPI.update_with_media("imgToTweet.jpg")
        return "ok", 200

    return "ok", 200
