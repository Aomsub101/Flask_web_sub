from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def testing():
    return "<p>Testing stuff</p>"

@app.route("/sum/<int:num1>/<int:num2>")
def get_sum(num1, num2):
    result = num1**2 + num2**2
    return f"<p>The sum of {num1}^2 + {num2}^2 = {result}</p>"