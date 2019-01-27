from flask import Flask, request, render_template
import sys, json, os, urllib, random
from config.twitter_client import getAPI
import praw, random, requests
from prawcore import NotFound as subNotFound
from urllib.request import Request, urlopen
from urllib.parse import urlencode

app = Flask(__name__)

if  os.path.exists("/config/bot.key.txt"):
    file = open("config/bot.key.txt",'r')
    BOT_ID = file.readline().strip("\n")
else:
    BOT_ID = os.getenv('bot_id')



twitterAPI = getAPI()

if os.path.exists("/config/reddit.key.txt"):
    file = open("config/reddit.key.txt", 'r')
    redditID = file.readline().strip("\n")
    redditSec = file.readline().strip("\n")
    redditAPI = praw.Reddit(client_id = redditID, client_secret = redditSec, user_agent = 'my user agent')
    file.close()
else:
    redditAPI = praw.Reddit(client_id = os.getenv('redditID'), client_secret = os.getenv('redditSecret'), user_agent = 'my user agent')

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
    return render_template('index.html')

@app.route('/recieve', methods=['POST'])
def recieveMessage():
    data = request.get_json()

    if ("@bot#tweet: " in data['text']):
        stringToTweet = data['text'].replace("@bot#tweet: ", "")
        twitterAPI.update_status(stringToTweet)
        return "ok", 200

    if ("@bot#pic: " in data['text']):
        sub = data['text'].replace("@bot#pic: ", "")
        sub.strip(" ")
        if (subreddit_exists(sub)):
            submissions = list(redditAPI.subreddit(sub).hot(limit=150))
            size = len(submissions)
            url = submissions[random.randint(0,size)].url
            count = 0
            while (".jpg" not in url) and count < 1000:
                url = submissions[random.randint(0,size)].url
                count += 1

            req = requests.get(url)
            with open('imgToTweet.jpg', 'wb') as openFile:
                openFile.write(req.content)
            try:
                twitterAPI.update_with_media("imgToTweet.jpg")
            except:
                print("inside exception")
                respond("oh no something went wrong. your command did not work")
        else:
            respond("subreddit not found for " + sub)

        return "ok", 200

    return "ok", 200
