import pandas as pd  
import numpy as np

import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

# Create a set with stopwords from ntkl and personalized dict
stops = set(stopwords.words("english"))   
custom_words = ['use','would','x','want','way','like','work','get','one',
                'new','code','need','someth','test','good','make','always',
                'problem','take','best','anyone','given','look','also',
                'well','give','user','value','without','know','abcde',
                'any','does','exampl','try','ani','do','doe','e','v','j'
                'file','will', 'hi', 'hello','question']   
stop_words = stops.union(set(custom_words))


def body_clean(title, text):
    body = [title + text]
    body = ''.join(body)
    body = re.sub('\+\+','plusplus', body) 
    body = re.sub('#','sharp', body)
    letters_only = re.sub("[^a-zA-Z]", " ", body)  
    words = letters_only.lower().split()         
    words = [w for w in words if not w in stop_words] 
    wnl = WordNetLemmatizer()
    words = [wnl.lemmatize(w) for w in words]
    stemmer = SnowballStemmer("english")
    words = [stemmer.stem(word) for word in words]      
    words = [w for w in words if not w in stop_words]
    return ( " ".join(words))

def tags_prediction(body):
    X = pd.Series(body)
    # TF-IDF Vectorization
    tfidf = joblib.load('tfidf_model.sav')
    X = tfidf.transform(X)
    # Multilabelled tags
    mlb = joblib.load('multilabelling_model.sav')
    # Linear SVC model
    svc_model = joblib.load('finalized_model.sav')
    pred_svc = svc_model.predict(X)
    # Visualization of tags
    return mlb.inverse_transform(pred_svc)