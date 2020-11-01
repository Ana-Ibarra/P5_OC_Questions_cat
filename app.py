import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'}

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Questions Classification Stackoverflow'),
    html.Div(children='''
        P5: A web application framework, from Openclassroom .
    '''),
    dcc.Input(
        id='input-1-state', type='text', value='Title', 
        style={'width': '80%', 'marginBottom': 10, 'marginTop': 10}), 
#     dcc.Textarea(
#         id='input-1-state', value='Title', style={'width': '100%', 'height': 50}), 
    dcc.Textarea(
        id='input-2-state', value='Text', style={'width': '100%', 'height': 300}),
   
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state', style={'whiteSpace': 'pre-line'})
    ])

# @app.callback(Output('output-state', 'children'),
#               [Input('submit-button-state', 'n_clicks')],
#               [State('input-1-state', 'value'),
#                State('input-2-state', 'value')])

# def update_output('input-1-state','input-2-state'):
#     body = body_clean('input-1-state', 'input-2-state')
#     output = tags_prediction(body)
#     return output

if __name__ == '__main__':
    app.run_server(debug=True)