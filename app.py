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


@app.callback(Output('Tags_output', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        from functions2 import body_clean
        from functions2 import tags_prediction
        body = body_clean(input1, input2)
        output = tags_prediction(body)
    return 'Your tags are : \n{}'.format(input1)


if __name__ == '__main__':
    app.run_server(debug=True)