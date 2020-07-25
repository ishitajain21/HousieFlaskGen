from flask import Flask,url_for
from flask import render_template
from flask import request
app = Flask(__name__)

# # @app.route('/hello/')
# # @app.route("/hello/<name>")
# # def hello(name=None):
# #     return render_template('hello.html',name=name)

from flask import abort, redirect, url_for

# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

# from flask import render_template

# @app.errorhandler(404)
# def page_not_found(error):
    
#     return render_template('yes.html'), 404

@app.route('/base',methods=['GET','POST'])
def index():
#    error = None
    if request.method == 'POST':
        print ("inside POST Method")
        print(request.form['lb1'])
        
                        
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('base.html')
    


# with app.test_request_context('/hello', method='GET'):
#     assert request.path == '/hello'
#     assert request.method == 'GET'


# # @app.route('/projects/')
# # def projects():
# #     return "The project page:))))"

# # @app.route('/user/<name>')
# # def show_user(name):
# #     return("USER:",name)


# # @app.route('/about')
# # def about():
# #     return "The about Page:::::::::::::::::::::::"

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# # with app.test_request_context():
# #     print(url_for('index'))
# #     print(url_for('login'))
# #     print(url_for('login',next='/'))
# #     print(url_for('profile',username='John Doe'))

# url_for('static',filename='style.css')

# # @app.route('/login',methods=['GET','POST'])
# # def login():
# #     if request.method == 'POST':
# #         return "POST"
# #     else:
# #         return "GET"