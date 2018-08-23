# Distribution Plots
# Layer three plots on top of one another.
# First histogram, where each data point is placed inside a bin of similar values
# Second histogram, rug plot - marks are placed along the x-axis for every data point, which lets you see the distribution of values inside each bin
# Third histogram, kernel density estimate, or KDE line that tries to describes the shape of the distribution

import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1,x2,x3,x4]
group_labels = ['X1','X2','X3','X4']

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels,bin_size=[.2,.1,.3,.4])
pyo.plot(fig, filename='04_plotly_15.html')

