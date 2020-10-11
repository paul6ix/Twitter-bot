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

FILE_NAME = 'saved_tweets.txt'


def check_saved_tweets(fl):
    read_file = open(fl, 'r')
    saved_tweet_id = int(read_file.read().strip())
    read_file.close()
    return saved_tweet_id


def save_tweet_id(file, ids):
    write_file = open(file, 'w')
    write_file.write(str(ids))
    write_file.close()
    return


def retweet():
    tweets = api.home_timeline(check_saved_tweets(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#End' in tweet.full_text:
            # print(str(tweet.id) + ' -- ' + tweet.full_text)
            # How to reply tweet and retweet
            # api.update_status(
            #     '@' + tweet.user.screen_name + ' Keep Retweeting the Hashtag #EndSARS #EndSarsNow #EndSARSBrutality ',
            #     tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            save_tweet_id(FILE_NAME, tweet.id)


while True:
    try:
        retweet()
        print('Bot is running: Retweeting & liking tweets relating to SARS')
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
