# Bubble Chart
# Similar to scatterplots, except we now convey a third variable's information through the size of the markers
# We can also continue to add variable information by coloring points based on a category

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')

data = [
    go.Scatter(
        x=df['horsepower'],
        y=df['mpg'],
        text=df['name'],
        mode='markers',
        marker=dict(
            # size=2*df['cylinders'],
            size=df['weight']/100,
            color=df['cylinders'],
            showscale=True
        )
    )
]

layout = go.Layout(title='Bubble Chart', hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='04_plotly_08.html')
