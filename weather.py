import sys
import tweepy
import pandas as pd
import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn import naive_bayes
from nltk.tokenize import RegexpTokenizer



consumer_key="zfFmnuYVmm3FlcYCrpznVSAP1"
consumer_secret="kld0SnBuxeUyCTIodjfCcDHRQldBffoSB6CW8wKHzp6pkWH2w0"
access_key="814501693324935168-BVQ3T3La5rcscE4Otl0zFoPMnQtp0Nd"
access_secret="8UvQH3UTaSA9dZFbWUkGo0Qk2gL0Pw1bTRioDteS9cWaq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet=[]
        if 'rain' in status.text.lower():
            tweet=status.text
            print (tweet)
            Save_this = str(time.time()) + '::' + tweet
            Save_File = open('weather1.json', 'a')
            Save_File.write(Save_this)
            Save_File.write('\n')
            Save_File.close()

    def on_error(self, status_code):
        print >> (sys.stderr, 'Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print >> (sys.stderr, 'Timeout...')
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[-6.38,49.87,1.77,55.81])
