# try:
#     from collections.abc import Callable  # noqa
# except ImportError:
#     from collections import Callable  # noqa


# import collections
# try:
#     collectionsAbc = collections.abc
# except AttributeError:
#     collectionsAbc = collections


#from six.moves import collections.abc
#from collections import abc
# from tokenize import String
# from bokeh.plotting import *
# from bokeh.models import *
# from random import random

# from bokeh.layouts import row
# from bokeh.models import ColumnDataSource, CustomJS, Button
# from bokeh.plotting import figure, output_file, show
# import FlowCal
# import matplotlib.pyplot as plt
# import holoviews
# #from ggplot import *
# from scipy import stats 
# import numpy as np
# import datetime
# import pandas as pd
# import datashader as ds
# import datashader.transfer_functions as tf
# import collections
# #from collections.abc import OrderedDict as odict
# import holoviews as hv

# from holoviews import opts
# import holoviews.operation.datashader
# from holoviews.operation.datashader import rasterize, datashade
# from holoviews.operation import decimate

# #C:\Users\Zuhayr\Documents\GitHub\r_background_app\venv
# #pip install -r /path/to/requirements.txt
# #--no-cache-dir

# begin_time = datetime.datetime.now()

# fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
# s = FlowCal.io.FCSData(fcsFile_filtered)[:1000]

# x1 = s[:, ['FSC-A']] 
# y1 = s[:, ['FSC-H']]


# z = np.column_stack((x1, y1))

# print(z)

# #points = hv.Points(z)
# #collections.abc.rasterize(points)
# #print(points)
# points = rasterize(z)
# #datashade(      points,      cmap="kbc_r", cnorm="linear").relabel("datashade()")
# #dict(x1=x1, y1=y1)

# # np_array = np.array(points)
# # print(np_array)
# print(points)
# df =  pd.DataFrame(points)
# print(df)
# s1 = ColumnDataSource(data=df)
# p1 = figure(width=400, height=400, tools="lasso_select, box_select, poly_select, pan, wheel_zoom, box_zoom, reset", title="Select Here")
# p1.xaxis.axis_label = 'FSC-A'
# p1.yaxis.axis_label = 'FSC-H'
# p1.circle('x', 'y', source=s1, alpha=0.6)
# #, color = density(x,y), color = "color column"

# print(datetime.datetime.now() - begin_time)

# layout = row(p1)
# #layout = row(p1)

# show(layout)

import numpy as np
import holoviews as hv
#from templates.holoviewsApp import dim, opts
import FlowCal
import panel as pn
import holoviews.operation.datashader as hvds
from matplotlib import cm
hv.extension("bokeh")


# fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
# s = FlowCal.io.FCSData(fcsFile_filtered)[:1000]

# # x1 = s[:, ['FSC-A']] 
# # y1 = s[:, ['FSC-H']]


# # z = np.column_stack((x1, y1))

# #point_opts = opts.Points(fill_color='#00AA00', fill_alpha=0.5, line_width=1, line_color='black', size=5)

# points = hv.Points(data=s, kdims=['FSC-A', 'FSC-H'])

# #stuff.opts(fill_color='blue', fill_alpha=0.5, size=5, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])

# hvds.dynspread(
#     hvds.datashade(
#         points, 
#         cmap=cm.Reds,
#     )
# ).opts(
#     width=350, 
#     height=300, 
#     padding=0.05,
#     show_grid=True,
# )

# #server = pn.serve(stuff, start=False, show=False)
# #server = pn.panel(stuff).show()
# #server.stop()



fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
s = FlowCal.io.FCSData(fcsFile_filtered)[:1000]
points =  hv.Points(data=s, kdims=['FSC-A', 'FSC-H'])

points.opts(fill_color='blue', fill_alpha=0.5, size=5, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])

server = pn.panel(points).show()