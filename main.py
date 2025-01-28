from flask import Flask, request, render_template
from markupsafe import escape
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


def graph(func_name, x):
    if func_name == 'sine':
        return np.sin(x)
    elif func_name == 'cosine':
        return np.cos(x)
    elif func_name == 'tangent':
        return np.tan(x)
    elif func_name == 'square':
        return x ** 2
    else:
        return np.sqrt(x)

@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        x_left = int(request.form['xleft'])
        x_right = int(request.form['xright'])
        x = np.linspace(x_left, x_right, 100)
        func_names = request.form.getlist('func')
        colors = request.form.getlist('color')
        separate = request.form.get('separate', 'off') == 'on'

        image_paths = []
        # print(func_names)
        # print(separate)
        # print(colors)

        if separate:
            for i, func in enumerate(func_names):
                y = graph(func, x)
                plt.plot(x, y, color=colors[i])
                plt.xlabel('X')
                plt.ylabel('y')
                plt.title(f'Graph of {func} from {x_left} to {x_right}')
                image_path = f'static/images/plot_{func}.png'
                plt.savefig(image_path)
                plt.close()
                image_paths.append(image_path)
        else:
            for i, func in enumerate(func_names):
                y = graph(func, x)
                plt.plot(x, y, color=colors[i], label=func)

            image_path = 'static/images/plot.png'
            plt.legend()
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.savefig(image_path)
            plt.title(f"Graph from {x_left} to {x_right}")
            plt.close()
            image_paths.append(image_path)
        return render_template('plotter.html', image_paths=image_paths)

    return render_template('plotter.html')

# End of file
