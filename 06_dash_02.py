import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

DF = pd.read_csv('data/mpg.csv')
APP = dash.Dash()
FEATURES = DF.columns

APP.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='xaxis',
            options=[
                dict(label=i, value=i) for i in FEATURES
            ],
            value='displacement'
        )
    ], style=dict(width='48%', display='inline-block')),
    html.Div([
        dcc.Dropdown(
            id='yaxis',
            options=[
                dict(label=i, value=i) for i in FEATURES
            ],
            value='mpg'
        )
    ], style=dict(width='48%', display='inline-block')),
    dcc.Graph(
        id='feature-graphic'
    )
], style=dict(padding=10))

@APP.callback(
    Output('feature-graphic', 'figure'),
    [
        Input('xaxis', 'value'),
        Input('yaxis', 'value'),
    ]
)
def update_graph(xaxis_name, yaxis_name):
    data = go.Scatter(
        x=DF[xaxis_name],
        y=DF[yaxis_name],
        text=DF['name'],
        mode='markers',
        marker=dict(
            size=15,
            opacity=0.5,
            line=dict(
                width=0.5,
                color='white'
            )
        )
    )
    layout = go.Layout(
        title='My Dashboard for MPG',
        xaxis=dict(title=xaxis_name),
        yaxis=dict(title=yaxis_name),
        hovermode='closest'
    )
    
    return dict(data=[data], layout=layout)

if __name__ == '__main__':
    APP.run_server()

