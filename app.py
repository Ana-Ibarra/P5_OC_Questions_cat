import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from functions import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server

style = {'maxWidth': '960px', 'margin': 'auto'}
app.layout = html.Div(children=[
    html.H1(children='Questions Classification Stackoverflow'),
    html.Div(children='''
        P5: A web application framework, from Openclassroom .
    '''),
    dcc.Input(
        id='input-1-state', type='text', placeholder='This is the title of the question', #value= 'Hi my name is Juan!',
        style={'width': '80%', 'marginBottom': 10, 'marginTop': 10}), 
   dcc.Textarea(
        id='input-2-state', placeholder='Here you have to put all the explanations about your questions including the description and so on...do no hesitate into use as many space as needed',
       #value='I want to know if my mom loves me or not but I use python and C++ to ask my java question',
       style={'width': '100%', 'height': 300}),
   
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='Tags_output', style={'whiteSpace': 'pre-line'})
    ])

    
@app.callback(Output('Tags_output', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0 and len(input1)>0 and len(input2)>0:
        body = body_clean(input1, input2)
        output = tags_prediction(body) 
        return u'''N click= {}, Your cleaned tags are : \n{} \n Tags: {}\n\n LO HICE!!'''.format(n_clicks,body,output)
    elif n_clicks == 0 :
        return u'''PLEASE TYPE SOME TEXT'''
    elif len(input1)==0 or len(input2)==0:
        return u'''PLEASE TYPE SOME TEXT'''
        

if __name__ == '__main__':
    app.run_server()