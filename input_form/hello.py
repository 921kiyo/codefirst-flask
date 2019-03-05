from flask import Flask, request, render_template

app = Flask("MyApp")

@app.route("/")
def show_hello ():
    return render_template("hello.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data=request.form
    print form_data["email"]
    return "All OK"


app.run(debug=True)
