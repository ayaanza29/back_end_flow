# holoviews.py
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
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

def first():
    fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
    s = FlowCal.io.FCSData(fcsFile_filtered)[:10000]
    x1 = s[:, ['FSC-A']] 
    y1 = s[:, ['FSC-H']]
    combined1 = (np.array(x1)).flatten()
    combined2 = (np.array(y1)).flatten()
    combined = pd.DataFrame({'FSC-A': combined1, 'FSC-H': combined2})
    combined = combined.to_numpy()
    ropts = dict(tools=["hover"], height=380, width=330, colorbar=True, colorbar_position="bottom")
    points = hv.Points(data=combined, kdims=['FSC-A', 'FSC-H']).opts(fill_color='blue', nonselection_color = "gray", fill_alpha=0.5, size=1, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])
    # selection = hv.streams.Selection1D(source=points)
    # def selected_info(index):
    #     arr = points.array()[index]
    #     if index:
    #         label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0))
    #     else:
    #         label = 'No selection'
    #     return points.clone(arr, label=label).opts(color='red')
    # selected_points = hv.DynamicMap(selected_info, streams=[selection])
    return points



def selected(stuff):
    selection = hv.streams.Selection1D(source=stuff)
    def selected_info(index):
        arr = points.array()[index]
        if index:
            label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0))
        else:
            label = 'No selection'
        return points.clone(arr, label=label).opts(color='red')
    selected_points = hv.DynamicMap(selected_info, streams=[selection])
    return selected_points

def graph(pos):
    if pos == 0:
        stuff = first()
        return first()
    elif pos == 1:
        print("hi")
        return selected(stuff)

if __name__ == '__main__':
    # dmap = hvds.dynspread(
    #     hvds.datashade(
    #         sine(), 
    #         cmap=cm.Reds,
    #     )
    # ).opts(
    #     width=350, 
    #     height=300, 
    #     padding=0.05,
    #     show_grid=True,
    # )
    print("hello")
    f = open("count_graph.txt", "r")
    count = int(f.read())
    f.close()
    points = graph(count)
    # points = rasterize(points)
    # ropts = dict(tools=["hover"], height=380, width=330, colorbar=True, colorbar_position="bottom")

    # dmap = (points).opts(**ropts).opts(fill_color='blue', nonselection_color = "gray", fill_alpha=0.5, size=5, frame_width=500, frame_height=500, tools=["lasso_select", "box_select", "poly_select"])
    # #selected(dmap._get_selection)
    # ropts = dict(tools=["hover"], height=380, width=330, colorbar=True, colorbar_position="bottom")
    # stuff = sine()
    # points = hv.Layout([rasterize(stuff).opts(**ropts).opts(cnorm=n).relabel(n)
    #         for n in ["linear", "log", "eq_hist"]])





    pn.serve(points, port=5006, allow_websocket_origin=["localhost:5000"], show=False)




# def sine(frequency, phase, amplitude):
#     xs = np.linspace(0, np.pi*4)
#     return hv.Curve((xs, np.sin(frequency*xs+phase)*amplitude)).options(width=800)

# if __name__ == '__main__':
#     ranges = dict(frequency=(1, 5), phase=(-np.pi, np.pi), amplitude=(-2, 2), y=(-2, 2))
#     dmap = hv.DynamicMap(sine, kdims=['frequency', 'phase', 'amplitude']).redim.range(**ranges)

#     pn.serve(dmap, port=5006, allow_websocket_origin=["localhost:5000"], show=False)