#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df = pd.read_csv('data/abalone.csv')

# create a data variable:
data = [
    go.Histogram(
        x=df['length'],
        xbins=dict(
            start=0,
            end=1,
            size=0.02
        ),
    )
]

# add a layout
layout = go.Layout(title='My Histogram')
fig = go.Figure(data=data, layout=layout)

# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='04_plotly_14.html')