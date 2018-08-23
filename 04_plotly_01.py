# Scatter plot allow the comparison of two variables for a set of data
# Depending on the trend of the scatter points, we could interpret a correlation
# Positive if A and B go Up
# Negative if A and B going Inverse

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x, y=random_y, mode='markers')]
layout = go.Layout(
    title='Hello First Plot', 
    xaxis = {'title':'MY X AXIS'},
    yaxis = dict(title='MY Y AXIS'),
    hovermode='closest'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename="04_plotly_01.html")

