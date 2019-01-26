from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    consumerKeyFile = open("APIkey.key.txt",'r')
    consumerSecretFile = open("APIsecret.key.txt",'r')
    accessSecretFile = open("AccessSecret.key.txt",'r')
    accessTokenFile = open("AccessToken.key.txt",'r')

    consumer_key = consumerKeyFile.readline()
    consumer_secret = consumerSecretFile.readline()
    access_token = accessSecretFile.readline()
    access_secret = accessTokenFile.readline()
    

    consumerKeyFile.close()
    consumerSecretFile.close()
    accessSecretFile.close()
    accessTokenFile.close()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client

def getAPI():
    return API(get_twitter_auth())