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


# output_file("toolbar.html")

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

x2 = x1 
y2 = s[:, ['FSC-W']]

x3 = y1 
y3 = y2

#x3_4 = s[:, ['SSC-A']] 
x3_4 = []
y3_4 = s[:, ['FSC-W']]

x4 = s[:, ['SSC-A']] 
y4 = s[:, ['SSC-H']]

x5 = x1
y5 = s[:, ['SSC-W']]

x6 = y4
y6 = y5

palette = ["#053061", "#2166ac", "#4393c3", "#92c5de", "#d1e5f0",
           "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]

palette2 = ["red", "orange", "yellow", "green", "purple"]




# density = x["melting point"]
# low = min(melting_points)
# high = max(melting_points)
# melting_point_inds = [int(10*(x-low)/(high-low)) for x in melting_points] #gives items in colors a value from 0-10
# elements['melting_colors'] = [palette[i] for i in melting_point_inds]

# melting_point_inds = [int(10*(x-low)/(high-low)) for x in melting_points]
# density = [palette[i] for i in melting_point_inds]

# def density(r, s):

#     return palette[i] 
#stats.gaussian_kde

# new = []
# for i in range(len(s)):
#     new.append("red")


s1 = ColumnDataSource(data=dict(x1=x1, y1=y1))

new = []
for i in range(len(x1)):
    # print(s1.data['x'])
    # print(s1.data['y'])
    # print(np.isinf(s1.data['x']).any())
    # an_array = s1.data['x']
    # norm = np.linalg.norm(an_array)
    # normal_array = an_array/norm
    # print(stats.gaussian_kde(s1.data['x'], i))
    new.append(palette2[3])


s1.data["color column"] = new
p1 = figure(width=400, height=400, tools="lasso_select, poly_select, pan, wheel_zoom, box_zoom, reset", title="Select Here")
p1.xaxis.axis_label = 'FSC-A'
p1.yaxis.axis_label = 'FSC-H'
p1.circle('x1', 'y1', source=s1, alpha=0.6, color = "color column")
#, color = density(x,y)

print(datetime.datetime.now() - begin_time)

s2 = ColumnDataSource(data=dict(x2=x2, y2=[]))
p2 = figure(width=400, height=400, tools="pan, wheel_zoom,lasso_select, poly_select", title="Watch Here")
p2.xaxis.axis_label = 'FSC-A'
p2.yaxis.axis_label = 'FSC-W'
p2.circle('x2', 'y2', source=s2, alpha=0.6)


s3 = ColumnDataSource(data=dict(x3=[], y3=y3))
p3 = figure(width=400, height=400, tools="pan, wheel_zoom,lasso_select, poly_select", title="Watch Here")
p3.xaxis.axis_label = 'FSC-H'
p3.yaxis.axis_label = 'FSC-W'
p3.circle('x3', 'y3', source=s3, alpha=0.6)



s3_4 = ColumnDataSource(data=dict(x3_4=[], y3_4=y3_4))
p3_4 = figure(width=400, height=400, tools="pan, wheel_zoom,lasso_select, poly_select", title="Watch Here")
#s3_4.selected.indicies 
p3_4.xaxis.axis_label = 'SSC-A'
p3_4.yaxis.axis_label = 'FSC-W'
p3_4.circle('x3_4', 'y3_4', source=s3_4, alpha=0.6)


s4 = ColumnDataSource(data=dict(x4=[], y4=y4))
p4 = figure(width=400, height=400, tools="pan, wheel_zoom,lasso_select, poly_select", title="Watch Here")
p4.xaxis.axis_label = 'SSC-A'
p4.yaxis.axis_label = 'SSC-H'
p4.circle('x4', 'y4', source=s4, alpha=0.6)

s5 = ColumnDataSource(data=dict(x5=x5, y5=[]))
p5 = figure(width=400, height=400, tools="pan, wheel_zoom,lasso_select, poly_select", title="Watch Here")
p5.xaxis.axis_label = 'SSC-A'
p5.yaxis.axis_label = 'SSC-W'
p5.circle('x5', 'y5', source=s5, alpha=0.6)


s6 = ColumnDataSource(data=dict(x6=[], y6=y6))
p6 = figure(width=400, height=400, tools="pan, wheel_zoom,lasso_select, poly_select", title="Watch Here")
p6.xaxis.axis_label = 'SSC-H'
p6.yaxis.axis_label = 'SSC-W'
p6.circle('x6', 'y6', source=s6, alpha=0.6)


#button = Button(label="Button", button_type="success")




s1.selected.js_on_change('indices', CustomJS(args=dict(s1=s1, s2=s2), code="""
        const inds = cb_obj.indices;
        const d1 = s1.data;
        const d2 = s2.data;
        d2['x2'] = []
        d2['y2'] = []
        for (let i = 0; i < inds.length; i++) {
            d2['x2'].push(d1['x1'][inds[i]])
            d2['y2'].push((d1['y1'])[inds[i]])
            
        }
        s2.change.emit();
    """)
)

s2.selected.js_on_change('indices', CustomJS(args=dict(s2=s2, s3=s3), code="""
        const inds = cb_obj.indices;
        const d2 = s2.data;
        const d3 = s3.data;
        d3['x3'] = []
        d3['y3'] = []
        for (let i = 0; i < inds.length; i++) {
          d3['x3'].push(d2['x2'][inds[i]])
          d3['y3'].push((d2['y2'])[inds[i]])
        }
        s3.change.emit();
    """)
)

s3.selected.js_on_change('indices', CustomJS(args=dict(s3=s3, s3_4=s3_4), code="""
        const inds = cb_obj.indices;
        const d3 = s3.data;
        const d3_4 = s3_4.data;
        d3_4['x3_4'] = []
        d3_4['y3_4'] = []
        for (let i = 0; i < inds.length; i++) {
          d3_4['x3_4'].push(d3['x3'][inds[i]])
          d3_4['y3_4'].push((d3['y3'])[inds[i]])
        }
        s3_4.change.emit();
    """)
)

s3_4.selected.js_on_change('indices', CustomJS(args=dict(s3_4=s3_4, s4=s4), code="""
        const inds = cb_obj.indices;
        const d3_4 = s3_4.data;
        const d4 = s4.data;
        d4['x4'] = []
        d4['y4'] = []
        for (let i = 0; i < inds.length; i++) {
          d4['x4'].push(d3_4['x3_4'][inds[i]])
          d4['y4'].push((d3_4['y3_4'])[inds[i]])
        }
        s4.change.emit();
    """)
)

# for (let i = 0; i < inds.length; i++) {
#           d4['x4'].push(d3_4['x3_4'][inds[i]])
#           d4['y4'].push((d3_4['y3_4'])[inds[i]])
#         }
s4.selected.js_on_change('indices', CustomJS(args=dict(s4=s4, s5=s5), code="""
        const inds = cb_obj.indices;
        const d4 = s4.data;
        const d5 = s5.data;
        d5['x5'] = []
        d5['y5'] = []
        for (let i = 0; i < inds.length; i++) {
          d5['x5'].push(d4['x4'][inds[i]])
          d5['y5'].push((d4['y4'])[inds[i]])
        }
        s5.change.emit();
    """)
)

s5.selected.js_on_change('indices', CustomJS(args=dict(s5=s5, s6=s6), code="""
        const inds = cb_obj.indices;
        const d5 = s5.data;
        const d6 = s6.data;
        d6['x6'] = []
        d6['y6'] = []
        for (let i = 0; i < inds.length; i++) {
          d6['x6'].push(d5['x5'][inds[i]])
          d6['y6'].push((d5['y5'])[inds[i]])
        }
        s6.change.emit();
    """)
)
selected_nums = []

s6.selected.js_on_change('indices', CustomJS(args=dict(s6=s6, selected_nums=selected_nums), code="""
        selected_nums = cb_obj.indices;
        console.log(selected_nums)
    """)
)

def update(attrname, old, new):
  print(s6.data)


# def getStuff():
#   global s6
#   print(s6.data)


# for (let i = 0; i < inds.length; i++) {
#             d3['x3'].push(d2['x2'][inds[i]])
#             d3['y3'].push((d2['y2'])[inds[i]])
            
#         }
# s3.selected.js_on_change('indices', CustomJS(args=dict(s1=s1, s2=s2), code="""
#         const inds = cb_obj.indices;
#         const d1 = s1.data;
#         const d2 = s2.data;
#         d2['x2'] = []
#         d2['y2'] = []
#         for (let i = 0; i < inds.length; i++) {
#             d2['x2'].push(d1['x1'][inds[i]])
#             d2['y2'].push((d1['y1'])[inds[i]])
            
#         }
#         s2.change.emit();
#     """)
# )



layout = column(row(p1, p2, p3), row(p3_4, p4, p5, p6))
#layout = row(p1)

show(layout)

save(layout)