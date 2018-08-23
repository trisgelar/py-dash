# Histogram
# Display an accurate representation of the overall distribution of continuous feature
# To create a histogram, we divide the entire range of values of the continuous feature into a series of intervals.
# increasing bin size (decreased number of bins)

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')

data = [
    go.Histogram(
        x=df['mpg'],
        xbins=dict(
            start=0,
            end=50,
            size=2
        )
    )
]

layout = go.Layout(title='My Histogram')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='04_plotly_13.html')

