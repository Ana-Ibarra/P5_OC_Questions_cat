import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


app.layout = html.Div(children=[
    html.H1(children='Questions Classification Stackoverflow'),
    html.Div(children='''
        P5: A web application framework, from Openclassroom .
    '''),
    dcc.Input(
        id='input-1-state', type='text', value='Title', 
        style={'width': '80%', 'marginBottom': 10, 'marginTop': 10}), 
   dcc.Textarea(
        id='input-2-state', value='Text', style={'width': '100%', 'height': 300}),
   
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='update_output', style={'whiteSpace': 'pre-line'})
    ])


# def get_tags(value1,value2)
#     from functions2 import body_clean
#     from functions2 import tags_prediction
#     body = body_clean('input-1-state', 'input-2-state')
#     output = tags_prediction(body)
#     return "{}".format(output)    

@app.callback(
    Output('update_output', 'children'),
    [Input('submit-button-state', 'n_clicks')],
    [State('input-2-state', 'value')],
    [State('input-1-state', 'value')]
)
def update_output(*args):
    if n_clicks > 0:
        s=['input-2-state','input-1-state']
        return 'You have entered: \n{}'.format(s)




if __name__ == '__main__':
    app.run_server(debug=True)