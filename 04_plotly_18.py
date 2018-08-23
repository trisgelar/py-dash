# Heatmaps
# allow visualization of 3 features
# Categorical or continuous features along the x and y axis to make up a grid, and then a 3rd continuous feature displayed through color

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/2010SantaBarbaraCA.csv')
# df = pd.read_csv('data/2010YumaAZ.csv')

data = [
    go.Heatmap(
        x=df['DAY'],
        y=df['LST_TIME'],
        z=df['T_HR_AVG'].values.tolist(),
        colorscale='Jet'
    )
]

layout = go.Layout(title='SB CA Temps')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='04_plotly_18.html')

