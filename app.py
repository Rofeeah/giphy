# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

# add route for giph results

@app.route("/yourgif",methods = ['GET', 'POST'] )
def yourgif():
    # gets the giph for giphy and puts the link on webpage
    
    user_response = request.form['gifchoice']
    
    giph_link = getImageUrlFrom(user_response)
    print(giph_link)
    # pass url to render template and have that url appear as an image in yourgif.html
    return render_template("yourgif.html",time = datetime.now(), giph_link = giph_link)
    # datetime.now gets the updated time and code for css. Tricks browser in updating to think its real time.

# print(request.form['gifchoice'])
