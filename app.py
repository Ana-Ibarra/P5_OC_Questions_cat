import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


app.layout = html.Div(children=[
    html.H1(children='Questions Classification Stackoverflow'),
    html.Div(children='''
        P5: A web application framework, from Openclassroom .
    '''),
    dcc.Input(
        id='input-1-state', type='text', value='Hi my name is Juan!', 
        style={'width': '80%', 'marginBottom': 10, 'marginTop': 10}), 
   dcc.Textarea(
        id='input-2-state', value='I want to know if my mom loves me or not but I use python and C++ to ask my java question', style={'width': '100%', 'height': 300}),
   
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='Tags_output', style={'whiteSpace': 'pre-line'})
    ])

###**********************************************************#####
###
###**********************************************************#####

import pandas as pd  
import numpy as np

import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
# from bs4 import BeautifulSoup

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

###**********************************************************#####
###
###**********************************************************#####


@app.callback(Output('Tags_output', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        body = body_clean(input1, input2)
#         output = tags_prediction(body) ### esta llinea ya no la hace...hay que verificar la funcion 
        return u'''N click= {}, Your tags are : \n{}'''.format(n_clicks,body)


if __name__ == '__main__':
    app.run_server(debug=True)