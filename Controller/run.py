from flask import Flask, render_template
from jetbot import Robot
import ipywidgets.widgets as widgets
from IPython.display import display
import traitlets
import time

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('index.html')

@app.route('/move/<direction>')

def move(direction):
    robot = Robot()
    if direction == "forward":
        robot.forward(0.4)
        time.sleep(0.5)
        robot.stop()
        return render_template('index.html')
    elif direction == "left":
        robot.left(0.3)
        time.sleep(0.5)
        robot.stop()
        return render_template('index.html')
    elif direction == "right":
        robot.right(0.3)
        time.sleep(0.5)
        robot.stop()
        return render_template('index.html')
    elif direction == "backward":
        robot.backward(0.4)
        time.sleep(0.5)
        robot.stop()
        return render_template('index.html')
    else:
        return render_template('index.html')
    return render_template('index.html')

if __name__== '__main__':
    app.run(host='0.0.0.0',port=1994)

