# from flask import Flask, flash, request, redirect, url_for, render_template
# import datetime
# import os
# import subprocess
# from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = "C:/Users/rkhan/Desktop/Z Research Programming"
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'fcs'}

# app = Flask(__name__, static_url_path='/static')
# app.config["Upload_Folder"] = UPLOAD_FOLDER

# @app.route("/")
# def index():
#     # Load current count
#     f = open("count.txt", "r")
#     count = int(f.read())
#     f.close()

#     # Increment the count
#     count += 1

#     # Overwrite the count
#     f = open("count.txt", "w")
#     f.write(str(count))
#     f.close()


#     current_date = datetime.datetime.now()
#     g = open("current_date.txt", "w")
#     g.write(str(current_date))
#     g.close()

#     # Render HTML with count variable
#     return render_template("index.html", count=count, current_date=current_date)

# @app.route('/index.html')
# def returningToIndex():
#     return render_template('index.html')

# @app.route('/login.html')
# def login():
#     return render_template('login.html')

# @app.route('/pca.html')
# def pca():
#     return render_template('pca.html')

# @app.route('/settings.html')
# def settings():
#     return render_template('settings.html')

# #@app.route('/upload.html')
# #def upload():
# #    return render_template('upload.html')
# """"
# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
# """
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload.html', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join("C:/Users/rkhan/Desktop/Z Research Programming", filename))
#             return redirect(url_for('upload_file', name=filename))
#     return render_template("uploadFormat.html")
    
    
    
#     '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''



# #pytho -m venv venv
# #venv\Scripts\activate
# #localhost:5000  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

# if __name__ == "__main__":
#     app.run(debug = True)


from tokenize import String
from bokeh.plotting import *
from bokeh.models import *
from random import random

from bokeh.layouts import row
from bokeh.models import ColumnDataSource, CustomJS, Button
from bokeh.plotting import figure, output_file, show
import FlowCal
import matplotlib.pyplot as plt
import holoviews
#from ggplot import *
from scipy import stats
import numpy as np
import datetime
import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
from collections.abc import *
import holoviews as hv

from holoviews import opts
from holoviews.operation.datashader import rasterize
from holoviews.operation import decimate


begin_time = datetime.datetime.now()

fcsFile_filtered = "C:/Users/Zuhayr/Documents/GitHub/r_background_app/PeacoQC_results/fcs_files/776 F SP_QC.fcs"
s = FlowCal.io.FCSData(fcsFile_filtered)[:1000]

x1 = s[:, ['FSC-A']] 
y1 = s[:, ['FSC-H']]


z = np.column_stack((x1, y1))


print(type(z))

points = hv.Points(z)
rasterize(points)



# s1 = ColumnDataSource(data=dict(x1=x1, y1=y1))
# p1 = figure(width=400, height=400, tools="lasso_select, box_select, poly_select, pan, wheel_zoom, box_zoom, reset", title="Select Here")
# p1.xaxis.axis_label = 'FSC-A'
# p1.yaxis.axis_label = 'FSC-H'
# p1.circle('x1', 'y1', source=s1, alpha=0.6, color = "color column")
# #, color = density(x,y)

# print(datetime.datetime.now() - begin_time)