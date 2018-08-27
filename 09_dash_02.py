import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(
        id='my_stock_picker',
        value='TSLA'
    ),
    dcc.Graph(
        id='my_graph',
        figure = dict(
            data=[
                dict(
                    x=[1,2],
                    y=[3,1]
                )
            ],
            layout=dict(
                title="Stock Ticker"
            ),
        )

    )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_stock_picker', 'value')]
)
def update_graph(stock_ticker):
    start = datetime(2017,1,1)
    end = datetime(2017,12,31)
    df = web.DataReader(stock_ticker, 'iex', start, end)
    fig = dict(
        data=[
            dict(
                x=df.index,
                y=df['close']
            )
        ],
        layout=dict(
            title=stock_ticker
        ),
    )
    return fig

if __name__ == '__main__':
    app.run_server()