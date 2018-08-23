# Distribution Plots
# Layer three plots on top of one another.
# First histogram, where each data point is placed inside a bin of similar values
# Second histogram, rug plot - marks are placed along the x-axis for every data point, which lets you see the distribution of values inside each bin
# Third histogram, kernel density estimate, or KDE line that tries to describes the shape of the distribution

import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data = [snodgrass,twain]
group_labels = ['Snodgrass Writings','Mark Twain Writtings']

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels,bin_size=[.005,.005])
pyo.plot(fig, filename='04_plotly_16.html')

