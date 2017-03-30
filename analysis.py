import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.decomposition import TruncatedSVD
from nltk.tokenize import RegexpTokenizer
import numpy as np



''''''''''
H_vocab='hot','sunny','heat','sunshine','boiling','Dry'
C_vocab='cold','winter','rain','freezing'
'''''

data= open('/home/alon/PycharmProjects/untitled1/weather1.json','r').read()

#our vocabulary, not the full list 

vocabulary='cold','winter','sunny','windy','rain','freezing','cloudy','foggy','humid','overcast','scorching','Fog','Dry','sunshine','boiling'

#after we gatherd all the data we need we need to tokenize each sentece so the computer could understand every word.

def tokenize_tweet(data):
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(data)
    return tokens
data=tokenize_tweet(data)
# than we use vectorizer from sklearn.

vectorizer=TfidfVectorizer(stop_words='english',
                           vocabulary=vocabulary,
                           lowercase=True,
                           use_idf=True)

X=vectorizer.fit_transform(data).toarray()
lsa=TruncatedSVD(n_components=1,n_iter=100)
lsa.fit(X)
terms=vectorizer.get_feature_names()
vocab=np.array(terms)
X_train = vectorizer.fit_transform(data)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))



print(lsa.components_)
for i,comp in enumerate(lsa.components_):
  termsInComp=zip(terms,comp)
  sortedTerms=sorted(termsInComp, key=lambda x:x[1], reverse=True) [:1]
  print ("concept %d:" % i)
  for term in sortedTerms:
    print ("the weather in england is:"+term[0])
  print (" ")


'''
at the out put we can see the size of our json file and the amount of words and the word that the 
computer saw that apears the most in our file.
''' 
