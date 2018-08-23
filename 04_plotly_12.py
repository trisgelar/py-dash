#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df = pd.read_csv('data/abalone.csv')

# take two random samples of different sizes:
a = np.random.choice(df['rings'], 30, replace=False)
b = np.random.choice(df['rings'], 20, replace=False)


# create a data variable with two Box plots:
data = [
    go.Box(
        y=a,
        name='Box1'
    ),
    go.Box(
        y=b,
        name='Box1'
    )
]

# add a layout
layout = go.Layout(title='My Boxplot')
fig = go.Figure(data=data, layout=layout)

# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='04_plotly_12.html')
