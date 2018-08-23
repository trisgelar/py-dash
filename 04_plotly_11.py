import plotly.offline as pyo
import plotly.graph_objs as go


snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [
    go.Box(
        y=snodgrass,
        # boxpoints='all',
        boxpoints='outliers',
        jitter=0.3,
        pointpos=0,
        name='Snodgrass'
    ),
    go.Box(
        y=twain,
        # boxpoints='all',
        boxpoints='outliers',
        jitter=0.3,
        pointpos=0,
        name='Twain'
    )
]

layout = go.Layout(title="My Box Plot")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='04_plotly_11.html')