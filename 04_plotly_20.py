import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/flights.csv')

data = [
    go.Heatmap(
        x=df['year'],
        y=df['month'],
        z=df['passengers'].values.tolist(),
        colorscale='Jet'
    )
]

layout = go.Layout(title='Flights')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='04_plotly_20.html')

