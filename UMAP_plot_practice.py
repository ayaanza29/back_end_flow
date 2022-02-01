# import sklearn.datasets
# import pandas as pd
# import numpy as np
# import umap
# #import umap.plot


# pendigits = sklearn.datasets.load_digits()
# mnist = sklearn.datasets.fetch_openml('mnist_784')
# fmnist = sklearn.datasets.fetch_openml('Fashion-MNIST')

# mapper = umap.UMAP().fit(fmnist.data[:30])

# umap.plot.points(mapper, labels=pendigits.target)

# hover_data = pd.DataFrame({'index':np.arange(30),
#                            'label':fmnist.target[:30]})
# hover_data['item'] = hover_data.label.map(
#     {
#         '0':'T-shirt/top',
#         '1':'Trouser',
#         '2':'Pullover',
#         '3':'Dress',
#         '4':'Coat',
#         '5':'Sandal',
#         '6':'Shirt',
#         '7':'Sneaker',
#         '8':'Bag',
#         '9':'Ankle Boot',
#     }
# )

# umap.plot.output_notebook()
# p = umap.plot.interactive(mapper, labels=fmnist.target[:30], hover_data=hover_data, point_size=2)
# umap.plot.show(p)

#################     Above works I think but takes forever

from bokeh.plotting import *
from bokeh.models import *

output_file("toolbar.html")

# # configure so that no drag tools are active
# p.toolbar.active_drag = None

# # configure so that Bokeh chooses what (if any) scroll tool is active
# p.toolbar.active_scroll = "auto"

# # configure so that a specific PolySelect tap tool is active
# p.toolbar.active_tap = poly_select

# # configure so that a sequence of specific inspect tools are active
# # note: this only works for inspect tools
# p.toolbar.active_inspect = [hover_tool, crosshair_tool]





# p = figure(tools="pan,lasso_select,box_select", active_drag="lasso_select")

# p = figure(tools="pan,wheel_zoom,box_zoom,reset")
# p.add_tools(BoxSelectTool(dimensions="width"))
# p.add_tools(LassoSelectTool())
# p.add_tools(PolySelectTool())
# p.add_tools(HoverTool())
# p.add_tools(CrosshairTool())



# # create a new plot with the toolbar below
# p = figure(width=400, height=400,
#            title=None, toolbar_location="below",
#            toolbar_sticky=False, tools = "lasso_select", active_drag = "lasso_select")

# # p.add_tools(BoxSelectTool())
# #p.add_tools(LassoSelectTool())
# p.add_tools(PolySelectTool())
# # p.add_tools(HoverTool())
# # p.add_tools(CrosshairTool())

# p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

# show(p)
# print(p.selected.indicies)








from random import random

from bokeh.layouts import row
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.plotting import figure, output_file, show

output_file("callback.html")

x = [random() for x in range(500)]
y = [random() for y in range(500)]

s1 = ColumnDataSource(data=dict(x=x, y=y))
p1 = figure(width=400, height=400, tools="lasso_select, box_select, poly_select", title="Select Here")
p1.circle('x', 'y', source=s1, alpha=0.6)

s2 = ColumnDataSource(data=dict(x=[], y=[]))
p2 = figure(width=400, height=400, x_range=(0, 1), y_range=(0, 1),
            tools="", title="Watch Here")
p2.circle('x', 'y', source=s2, alpha=0.6)

s1.selected.js_on_change('indices', CustomJS(args=dict(s1=s1, s2=s2), code="""
        const inds = cb_obj.indices;
        const d1 = s1.data;
        const d2 = s2.data;
        d2['x'] = []
        d2['y'] = []
        for (let i = 0; i < inds.length; i++) {
            d2['x'].push(d1['x'][inds[i]])
            d2['y'].push(d1['y'][inds[i]])
        }
        s2.change.emit();
    """)
)

layout = row(p1, p2)

show(layout)