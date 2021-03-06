
from tokenize import String
from bokeh.plotting import *
from bokeh.models import *
from random import random

from bokeh.layouts import row, column
#from bokeh.models import ColumnDataSource, CustomJS, Button
#from bokeh.plotting import figure, output_file, show
import FlowCal
import matplotlib.pyplot as plt
#import templates.holoviewsApp as holoviewsApp
#from ggplot import *
from scipy import stats
import numpy as np
import datetime
import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
from collections import OrderedDict as odict


output_file("callback.html")

# x = [random() for x in range(500)]
# y = [random() for y in range(500)]

begin_time = datetime.datetime.now()
fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
s = FlowCal.io.FCSData(fcsFile_filtered)[:1000]

x1 = s[:, ['FSC-A']] 
y1 = s[:, ['FSC-H']]


s1 = ColumnDataSource(data=dict(x1=x1, y1=y1))


s1.data["color column"] = "blue"
p1 = figure(width=400, height=400, tools="lasso_select, poly_select, pan, wheel_zoom, box_zoom, reset", title="Select Here")
p1.xaxis.axis_label = 'FSC-A'
p1.yaxis.axis_label = 'FSC-H'
p1.circle('x1', 'y1', source=s1, alpha=0.6, color = "color column")