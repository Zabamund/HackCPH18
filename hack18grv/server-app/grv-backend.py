from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return jsonify({'text':'Hello World!'})

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
    app.run(port=5002)
