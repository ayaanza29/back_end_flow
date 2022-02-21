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

from pickle import TRUE
import numpy as np
import holoviews as hv
#from templates.holoviewsApp import dim, opts
import FlowCal
import panel as pn
import holoviews.operation.datashader as hvds
from holoviews.operation.datashader import datashade, shade, dynspread, spread, rasterize
from holoviews.operation import decimate
from matplotlib import cm
import pandas as pd
import numpy as np
from numba import jit
hv.extension("bokeh")
from scipy.stats import gaussian_kde

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
s = FlowCal.io.FCSData(fcsFile_filtered)[:10000]

x1 = s[:, ['FSC-A']] 
y1 = s[:, ['FSC-H']]

#combined = s[:, ['FSC-A', 'FSC-H']]
#combined = dict(combined)
combined1 = (np.array(x1)).flatten()
print(type(combined1))
print(combined1)
combined2 = (np.array(y1)).flatten()
print(type(combined2))
#print(.analysis)
#combined = {'x': combined1, 'y': combined2}


combined = pd.DataFrame({'FSC-A': combined1, 'FSC-H': combined2})
combined = combined.to_numpy()

print(combined)
# points =  hv.Points(data=s, kdims=['FSC-A', 'FSC-H'])
# points = rasterize(points)
# points.opts(fill_color='blue', fill_alpha=0.5, size=5, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])

ropts = dict(tools=["hover"], height=380, width=330, colorbar=True, colorbar_position="bottom")

points = hv.Points(data=combined, kdims=['FSC-A', 'FSC-H']).opts(fill_color='blue', nonselection_color = "gray", fill_alpha=0.5, size=1, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])
#points = hv.Bivariate(data=combined, kdims=['FSC-A', 'FSC-H']).opts(cmap='Blues', colorbar=True, filled=True, toolbar='above', width=350)
# points = hv.Layout([rasterize(stuff).opts(**ropts).opts(cnorm=n).relabel(n)
#            for n in ["linear", "log", "eq_hist"]])
# points = rasterize(hv.Points(data=s, kdims=['FSC-A', 'FSC-H'])).opts(fill_color='blue', fill_alpha=0.5, size=5, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])
#points = rasterize(points)
#points = rasterize(stuff)

# def update(attr ,old, new):
#     source.data = new
selection = hv.streams.Selection1D(source=points)
def selected_info(index):
    arr = points.array()[index]
    if index:
        label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0))
    else:
        label = 'No selection'
    return points.clone(arr, label=label).opts(color='red')
selected_points = hv.DynamicMap(selected_info, streams=[selection])
# points.on_change()
#points = gaussian_kde(points)
server = pn.serve(points + selected_points, start=TRUE, show=TRUE)
#server = pn.panel(points).show()



# num=10000
# np.random.seed(1)

# dists = {cat: pd.DataFrame(dict([('x',np.random.normal(x,s,num)), 
#                                  ('y',np.random.normal(y,s,num)), 
#                                  ('val',val), 
#                                  ('cat',cat)]))      
#          for x,  y,  s,  val, cat in 
#          [(  2,  2, 0.03, 10, "d1"), 
#           (  2, -2, 0.10, 20, "d2"), 
#           ( -2, -2, 0.50, 30, "d3"), 
#           ( -2,  2, 1.00, 40, "d4"), 
#           (  0,  0, 3.00, 50, "d5")] }

# df = pd.concat(dists,ignore_index=True)
# df["cat"]=df["cat"].astype("category")
# print(df)
# ropts = dict(tools=["hover"], height=380, width=330, colorbar=True, colorbar_position="bottom")

# points = hv.Layout([rasterize(hv.Points(df)).opts(**ropts).opts(cnorm=n).relabel(n)
#            for n in ["linear", "log", "eq_hist"]])

# server = pn.panel(points).show()