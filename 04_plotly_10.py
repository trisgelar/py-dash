# Box Plots
# Visualize the variation of feature by depicting teh continous numerical data through quartiles
# seperate data based on categorical feature to compare the continuous feature based on category
# IQR interquartile range (the length of the filled in box Q3-Q1)
# max and min values are shown with whiskers

import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        # boxpoints='all',
        boxpoints='outliers',
        jitter=0.3,
        pointpos=0
    )
]

layout = go.Layout(title="My Box Plot")
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='04_plotly_10.html')