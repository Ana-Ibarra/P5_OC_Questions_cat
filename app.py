import os

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
from functions import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {'background': '#a23530',
          'text': '#FFFFFF'}

app.config.suppress_callback_exceptions = True

server = app.server

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div(children=[
    html.H1(children="Project 5: Stackoverflow's questions classification"),
    html.Div(children='''
        A web application framework, from Openclassroom.
    '''),
    dcc.Input(
        id='input-1-state', type='text', placeholder='Title of the question', 
        value="How to log SQL statements in Spring Boot?"
        style={'width': '80%', 'marginBottom': 10, 'marginTop': 10,'backgroundColor': colors['background'],'color': colors['text']}), 
    dcc.Textarea(
        id='input-2-state', placeholder='Here write the question',
       value="I have the following properties. I can see statements in sping...",
       style={'width': '100%', 'height': 200,'backgroundColor': colors['background'],'color': colors['text']}),
   
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
        return u'''Your treated tags are : Tags: {}\n'''.format(output)
    elif n_clicks == 0 :
        return u'''PLEASE TYPE SOME TEXT'''
    elif len(input1)==0 or len(input2)==0:
        return u'''PLEASE TYPE SOME TEXT'''
        

if __name__ == '__main__':
    app.run_server(debug = True)