from tweepy import API
from tweepy import OAuthHandler
import os


def get_twitter_auth():

    if os.path.exists("./twitter.key.txt"):
        file = open("twitter.key.txt",'r')

        consumer_key = file.readline().strip('\n')
        consumer_secret = file.readline().strip('\n')
        access_token = file.readline().strip('\n')
        access_secret = file.readline().strip('\n')

        file.close()

    else:
        consumer_key = os.getenv('twitterConsumerKey')
        consumer_secret = os.getenv('twitterConsumerSecret')
        access_token = os.getenv('twitterAccessToken')
        access_secret = os.getenv('twitterAccessSecret')

    

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client

def getAPI():
    return API(get_twitter_auth())