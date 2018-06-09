from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def home():
    return jsonify({'text':'Hello World!'})

@app.route("/CORS")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/API', methods = ['GET'])
def apicall():
    if request.method == 'GET':
        dictionary = {'var1':request.args.get('arg1'),
                    'var2':request.args.get('arg2')}
    return jsonify(dictionary)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
