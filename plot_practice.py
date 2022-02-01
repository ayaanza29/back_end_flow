import numpy as np 
import pandas as pd 
import plotly.express as px
import bokeh as bk
import matplotlib as ml

class plot:
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def draw_graph(self):
        return 0


fig = figure()
ax1 = fig.add_subplot(111)
ax1.set_title('custom picker for line data')
line, = ax1.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)

line, = ax1.plot(rand(100), 'o', picker=5)  # 5 points tolerance