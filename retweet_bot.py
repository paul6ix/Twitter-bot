import os
import time

import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def retweet_hashtag():
    hashtag = '#SARS'
    tweet_number = 20
    tweets = tweepy.Cursor(api.search, hashtag).items(tweet_number)
    for tweet in reversed(tweets):
        tweet.retweet()


while True:
    try:
        retweet_hashtag()
        print('Bot is running: Retweeting & liking tweets relating to SARS')
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
