import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

df = pd.read_csv('data/OldFaithful.csv')
app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure=dict(
            data=[go.Scatter(
                x=df['X'],
                y=df['Y'],
                mode='markers'
            )],
            layout=go.Layout(
                title='Old Faithful Eruptions',
                xaxis=dict(
                    title='Duration'
                ),
                yaxis=dict(
                    title='Interval'
                )
            )
        )
    )
])

if __name__ == '__main__':
    app.run_server()