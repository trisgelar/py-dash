import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import base64

DF = pd.read_csv('data/wheels.csv')

APP = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(
        open(image_file, 'rb').read()
    )
    return 'data:image/png;base64,{}'.format(encoded.decode())

APP.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[dict(
            label=i,
            value=i,
        ) for i in DF['wheels'].unique()],
        value=1
    ),
    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(
        id='colors',
        options=[dict(
            label=i,
            value=i,
        ) for i in DF['color'].unique()],
        value='blue'
    ),
    html.Div(id='colors-output'),
    html.Img(
        id='display-image', 
        src='children',
        height=300
    )
], style=dict(
    fontFamily='helvetica',
    fontSize=18
))

@APP.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')]
)
def callback_a(wheels_value):
    return "you choose {}".format(wheels_value)

@APP.callback(
    Output('colors-output','children'),
    [Input('colors', 'value')])
def callback_b(colors_value):
    return "you choose {}".format(colors_value)

@APP.callback(
    Output('display-image', 'src'),
    [
        Input('wheels', 'value'),
        Input('colors', 'value'),
    ]
)
def callback_image(wheel, color):
    path = 'data/images/'
    return encode_image(path+DF[(DF['wheels']==wheel) & (DF['color']==color)]['image'].values[0])

if __name__ == '__main__':
    APP.run_server()