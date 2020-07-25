import functools

from flask import Blueprint, Flask
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# @app.route("/login", methods=("GET", "POST"))
# def login():
#     """ 
#     Log in a registered user by adding the user id to the session. 
#     """
#     username = None
#     #import pdb;pdb.set_trace() #interactive debugging /n to proceed, c for continue
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         # return render_template("login.html",username=username,password=password)       
#         print ("Inside POST method:", username, password)
#     if username != None:
#         request.form["username"] = username
#     return render_template("login.html")

# @app.route('/')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'YOU ARE NOT LOOGGEED INN!!!'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
            <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
# @app.route('/logout')
# def logout():
#     session.pop('username',None)
#     return redirect(url_for('index'))
