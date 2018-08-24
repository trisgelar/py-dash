import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

APP = dash.Dash()
APP.layout = html.Div([
    dcc.Input(id='number-in', value=1, style=dict(
        fontsize=24
    )),
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit Here',
        style=dict(
            fontsize=24
        )
    ),
    html.H1(id='number-out')
])

@APP.callback(
    Output('number-out', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('number-in', 'value')]
)

def output(n_clicks, number):
    return "{} was type in, and button was clicked {} times".format(number, n_clicks)

if __name__ == '__main__':
    APP.run_server()

