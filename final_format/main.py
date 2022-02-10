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


from __future__ import print_function
import json

from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.sampledata.iris import flowers

from flask import Flask
from jinja2 import Template

app = Flask(__name__)
