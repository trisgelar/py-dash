# Line
# Styles Line, Markers, Line+Markers
# Displays a series of data points connected by line segments
# Similar to a scatter plot except that the measurement points are ordered (typically by their x-axis values) and joined with straight line segments.
# Often used to visualize a trend in data over intervals of time - known as a time series

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace0 = go.Scatter(
    x=x_values, y=y_values+5,
    mode='markers',
    name='markers'
)

trace1 = go.Scatter(
    x=x_values, y=y_values,
    mode='lines',
    name='mylines'
)

trace2 = go.Scatter(
    x=x_values, y=y_values-5,
    mode='lines+markers',
    name='my favorite'
)

data = [trace0,trace1,trace2]

layout = go.Layout(title="Line Charts")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='04_plotly_03.html')

