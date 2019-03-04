from flask import Flask, render_template

from flask_login import login_required

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>", methods=["GET"])
def google_search(name):
    pass

@app.route("/result", methods=["POST"])
def google_search(name):
    pass

app.run(debug=True)
