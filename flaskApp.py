#flaskApp.py
from holoviewsApp import *
from bokeh.client import pull_session
from bokeh.embed import server_session
from flask import Flask, render_template
from flask import send_from_directory
import panel as pn
app = Flask(__name__)

# locally creates a page
@app.route('/')
def index():
    with pull_session(url="http://localhost:5006/") as session:
            # generate a script to load the customized session
            script = server_session(session_id=session.id, url='http://localhost:5006')
            # use the script in the rendered page
    return render_template("embed.html", script=script) #template="Flask"


@app.route('/page')
def page():
    with pull_session(url="http://localhost:5006/") as session:
            # generate a script to load the customized session
            script = server_session(session_id=session.id, url='http://localhost:5006')
            # use the script in the rendered page
    return render_template("page.html", script=script) #template="Flask"

# @app.route('/graph2')
# def graph2():
#     f = open("count_graph.txt", "r")
#     count = int(f.read())
#     f.close()
#     if count == 0:
#         count = 1
#     else:
#         count = 0
#     print("why")
#     # Overwrite the count
#     f = open("count_graph.txt", "w")
#     f.write(str(count))
#     f.close()
#     with pull_session(url="http://localhost:5006/") as session:
#             # generate a script to load the customized session
#             script = server_session(session_id=session.id, url='http://localhost:5006')
#             # use the script in the rendered page
#     return render_template("page.html", script=script) #template="Flask"


if __name__ == '__main__':
    # runs app in debug mode
    app.run(port=5000, debug=True)

#python templates/holoviewsApp.py  C:\Users\Zuhayr\Documents\GitHub\r_background_app\stuff\templates\embed.html
#python stuff/flaskApp.py