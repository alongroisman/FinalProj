import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.decomposition import TruncatedSVD

import numpy as np



data= open('/home/alon/PycharmProjects/untitled1/weather1.json','r').read()

vocabulary='cold','winter','sunny','rain','freezing','cloudy','foggy','humid','overcast','scorching'
'''
def tokenize_tweet(data):
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(data)
    return tokens
'''
vectorizer=TfidfVectorizer(stop_words='english',vocabulary=vocabulary,use_idf=True)

X=vectorizer.fit_transform(data)
lsa=TruncatedSVD(n_components=5,n_iter=100)
lsa.fit(X)

terms=vectorizer.get_feature_names()
for i,comp in enumerate(lsa.components_):
  termsInComp=zip(terms,comp)
  sortedTerms=sorted(termsInComp, key=lambda x:x[1], reverse=True) [:1]
  print ("concept %d:" % i)
  for term in sortedTerms:
    print (term[0])
  print (" ")
