import sys
import tweepy
import pandas as pd
import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn import naive_bayes
from nltk.tokenize import RegexpTokenizer

'''
our keys so we could download all the data from twitter.

'''
consumer_key="zfFmnuYVmm3FlcYCrpznVSAP1"
consumer_secret="kld0SnBuxeUyCTIodjfCcDHRQldBffoSB6CW8wKHzp6pkWH2w0"
access_key="814501693324935168-BVQ3T3La5rcscE4Otl0zFoPMnQtp0Nd"
access_secret="8UvQH3UTaSA9dZFbWUkGo0Qk2gL0Pw1bTRioDteS9cWaq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#this class is incharge of selecting which tweet will enter our file,and cleaning the tweet so there will be no unneceserry signs.

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet=[]
       # any(c in status.text.lower() for c in ("hot", "cold", "rain", "fog", "wather")):
        if 'rain' in status.text.lower() or 'hot' in status.text.lower() or 'weather' in status.text.lower() or 'cold' in status.text.lower() :
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

# currently we are following england coordinates, but it can be changed to any country we want.

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[-6.38,49.87,1.77,55.81])
