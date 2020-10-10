import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

FILE_NAME = 'saved_tweets.txt'


def check_saved_tweets(fl):
    read_file = open(fl, 'r')
    saved_tweet_id = int(read_file.read().strip())
    read_file.close()
    return saved_tweet_id


result = check_saved_tweets(FILE_NAME)


def save_tweet_id(file, ids):
    write_file = open(file, 'w')
    write_file.write(str(ids))
    write_file.close()
    return


save_tweet_id(FILE_NAME, result)

tweets = api.home_timeline()
for tweet in tweets:
    if '#End' in tweet.text:
        print('New tweet relating to SARS')
        print(str(tweet.id) + ' -- ' + tweet.text)
