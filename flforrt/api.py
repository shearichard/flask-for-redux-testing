from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api

todos = {}
app = Flask(__name__)
CORS(app)
api = Api(app)


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
