import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

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
    fig = dict(
        data=[
            dict(
                x=[1,2],
                y=[3,1]
            )
        ],
        layout=dict(
            title=stock_ticker
        ),
    )
    return fig

if __name__ == '__main__':
    app.run_server()