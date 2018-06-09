from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/')
def home():
    return jsonify({'text':'Hello World!'})

@app.route("/CORS")
def helloWorld():
  return "Hello, cross-origin-world!"

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
    app.run(port=5002)
