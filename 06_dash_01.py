'''[summary]

Returns:
    [type] -- [description]
'''

import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

DF = pd.read_csv('data/gapminderDataFiveYear.csv')

APP = dash.Dash()
YEAR_OPTIONS = []
for year in DF['year'].unique():
    YEAR_OPTIONS.append(dict(
        label=str(year),
        value=year
    ))

APP.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(
        id='year-picker',
        options=YEAR_OPTIONS,
        value=DF['year'].min()
    )
])

@APP.callback(
    Output('graph', 'figure'),
    [Input('year-picker', 'value')]
)
def update_figure(selected_year):
    filtered_df = DF[DF['year'] == selected_year]
    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(
            go.Scatter(
                x=df_by_continent['gdpPercap'],
                y=df_by_continent['lifeExp'],
                mode='markers',
                opacity=0.7,
                marker=dict(
                    size=15
                ),
                name=continent_name
            )
        )
    
    return dict(data=traces, layout=go.Layout(
        title='My Plot',
        xaxis=dict(title='GDP Per Cap', type='log'),
        yaxis=dict(title='Life Expectancy')
    ))

if __name__ == '__main__':
    APP.run_server()
