# holoviews.py

import holoviews as hv
from holoviews import opts
import panel as pn
import numpy as np
import holoviews.operation.datashader as hvds
from holoviews.operation.datashader import datashade, shade, dynspread, spread, rasterize
from matplotlib import cm
import FlowCal
hv.extension("bokeh")


hv.extension('bokeh')

def sine():
    fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
    s = FlowCal.io.FCSData(fcsFile_filtered)[:1000]
    ropts = dict(tools=["hover"], height=380, width=330, colorbar=True, colorbar_position="bottom")
    return hv.Points(data=s, kdims=['FSC-A', 'FSC-H'])

def selected(stuff):
    print(stuff)

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
    points = sine()
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