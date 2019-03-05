from flask import Flask, render_template

from flask_login import login_required
# from flask_mail import Message
from cat import print_cute_cat

app = Flask("MyApp")
# Create an instance of Flask class called "MyApp".
# If you want to know more about Python classes,
# see https://www.w3schools.com/python/python_classes.asp

# This is a Flask decorator.
# For decorators, see http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
@app.route("/")
def hello():
    return render_template("hello.html")


# @app.route("/profile")
# @login_required
# def show_profile():
#     return "My profile"


@app.route("/hello")
@app.route("/hello/<name>")
def pretty_hello(name):
    return render_template("hello.html", name=name)

app.run(debug=True)
