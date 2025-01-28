from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
@app.route("/hello/<name>")
def greeting(name=None):
    return render_template('greeting.html', name=name)

@app.route("/test")
def testing():
    return "<p>Testing stuff</p>"

@app.route("/sum/<int:num1>/<int:num2>")
def get_sum(num1, num2):
    result = num1**2 + num2**2
    return render_template('calculate.html', result=result)