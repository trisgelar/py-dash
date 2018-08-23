# Bar Charts
# Stacked Bar Charts
# Nested Bar Charts
# Presents categorical data with rectangular bars with heights (or lengths) propotional to the values that they represent.

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/2018WinterOlympics.csv')
data = []

# Simple Barchart
# trace = go.Bar(
#             x=df['NOC'],
#             y=df['Total'],
#     )
# data.append(trace)

# Nested Barchart
trace1 = go.Bar(
            x=df['NOC'],
            y=df['Gold'],
            name='Gold',
            marker=dict(
                color='#FFD700'
            )
    )
data.append(trace1)
trace2 = go.Bar(
            x=df['NOC'],
            y=df['Silver'],
            name='Silver',
            marker=dict(
                color='#9EA0A1'
            )
    )
data.append(trace2)
trace3 = go.Bar(
            x=df['NOC'],
            y=df['Bronze'],
            name='Bronze',
            marker=dict(
                color='#CD7F32'
            )
    )
data.append(trace3)

layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='04_plotly_06.html')