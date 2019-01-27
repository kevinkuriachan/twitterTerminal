from flask import Flask, request
import sys, json, os, urllib, random
from config.twitter_client import getAPI
import praw, random, requests
from prawcore import NotFound as subNotFound
from urllib.request import Request, urlopen

app = Flask(__name__)

BOT_ID = os.getenv('bot_id')



twitterAPI = getAPI()
redditAPI = reddit = praw.Reddit(client_id = os.getenv('redditID'), client_secret = os.getenv('redditSecret'), user_agent = 'my user agent')

def subreddit_exists(name):
    # reference: https://www.reddit.com/r/redditdev/comments/68dhpm/praw_best_way_to_check_if_subreddit_exists_from/
    exists = True
    try:
        redditAPI.subreddits.search_by_name(name, exact=True)
    except subNotFound:
        exists = False
    return exists

def respond(message):
    url = "https://api.groupme.com/v3/bots/post"
    data = {
				'bot_id' : BOT_ID,
				'text' : message,
			}
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


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

    if ("@bot#pic: " in data['text']):
        sub = data['text'].replace("@bot#pic: ", "")
        if (subreddit_exists(sub)):
            submissions = list(redditAPI.subreddit(sub).hot(limit=150))
            size = len(submissions)
            url = submissions[random.randint(0,size)].url
            req = requests.get(url)
            with open('imgToTweet.jpg', 'wb') as openFile:
                openFile.write(req.content)
            twitterAPI.update_with_media("imgToTweet.jpg")
        else:
            respond("subreddit not found for " + sub)

        return "ok", 200

    return "ok", 200
