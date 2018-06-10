# imports
from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

#routes

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

@app.route('/slider', methods = ['GET'])
def slider():
    if request.method == 'GET':
        slider_value = request.args.get('arg1')
        print('slider_value', slider_value)
        return slider_value


# run
if __name__ == '__main__':
    app.run(port=5002, debug=True)