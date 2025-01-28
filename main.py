from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
import matplotlib.pyplot as plt
import numpy as np

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

@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        x_left = int(request.form['xleft'])
        x_right = int(request.form['xright'])
        x = np.linspace(x_left, x_right, 100)

        if request.form['func'] == 'sine':
            y = np.sin(x)
        elif request.form['func'] == 'cosine':
            y = np.cos(x)
        elif request.form['func'] == 'tangent':
            y = np.tan(x)
        elif request.form['func'] == 'square':
            y = x ** 2
        else:
            y = np.sqrt(x)

        plt.title(f'Graph of {request.form['func']} from {x_left} to {x_right}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot(x, y)
        img_path = 'static/images/plot.png'
        plt.savefig(img_path)
        plt.close()
        return render_template('plotter.html', image_path=img_path)

    return render_template('plotter.html')

# End of file
