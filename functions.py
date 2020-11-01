import pandas as pd  
import numpy as np

import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup

def raw2string(raw2review):
    # Function to convert a raw to a string of words
    raw2review = BeautifulSoup(raw2review).get_text()       
    letters_only = re.sub("[^a-zA-Z]", " ", raw2review)   
    words = letters_only.lower().split()         
    words = [w for w in words if not w in stop_words] 
    wnl = WordNetLemmatizer()
    words = [wnl.lemmatize(w) for w in words]
    stemmer = SnowballStemmer("english")
    words = [stemmer.stem(word) for word in words]      
    words = [w for w in words if not w in stop_words]   
    return( " ".join(words)) 

def body_clean(title, text):

    body = title + text
    body = body.str.replace('\+\+','plusplus',regex=True)
    body = body.str.replace('#','sharp',regex=True)
    
    # Create a set with stopwords from ntkl and personalized dict
    stops = set(stopwords.words("english"))   
    custom_words = ['use','would','x','want','way','like','work','get','one',
                'new','code','need','someth','test','good','make','always',
                'problem','take','best','anyone','given','look','also',
                'well','give','user','value','without','know','abcde',
                'any','does','exampl','try','ani','do','doe','e','v','j'
                'file','will', 'hi', 'hello','question']   
    stop_words = stops.union(set(custom_words))
    
    body = raw2string(body)
    return body

def tags_prediction(body):

    # Preprocessing
    X = body.map(lambda text:[w for w in text.split() if w])

    # TF-IDF Vectorization
    tfidf = joblib.load('tfidf_model.sav')
    X = tfidf.transform(X)
    print(X.shape)

    # Multilabelled tags
    mlb = joblib.load('multilabelling_model.sav')

    # Linear SVC model
    svc_model = joblib.load('finalized_model.sav')
    pred_svc = svc_model.predict(X)

    # Visualization of tags
    return mlb.inverse_transform(pred_svc)