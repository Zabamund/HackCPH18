# imports
from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

#routes
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/minimal')
def minimal():
    return render_template('bootstrap-mini.html')

@app.route('/jinja_template')
def jinja_template():
    dictionary = {'company': 'Agile', 'country': 'Canada'}
    image_location = 'http://bit.ly/2mY5YUz'
    return render_template('jinja_template.html', logo=image_location, content=dictionary)

@app.route('/')
def home():
    dictionary = {'company': 'Agile', 'country': 'Canada'}
    image_location = 'http://bit.ly/2mY5YUz'
    return render_template('index.html', logo=image_location, content=dictionary)

# run
if __name__ == '__main__':
    app.run(port=5002, debug=True)