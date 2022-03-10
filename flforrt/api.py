from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import csv
import uuid
import pprint

app = Flask(__name__)
CORS(app)
api = Api(app)

MOVIE_INPUT_FIELD_NAMES = ['film', 'genre', 'lead_studio', 'audience_score_percent', 'profitability', 'rotten_tomatoes_percent', 'worldwide_gross_usd', 'year']

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}
MOVIES = None


def initialize_movies():
    dicout = {}
    with open('movies.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=MOVIE_INPUT_FIELD_NAMES)
        #
        for row in reader:
            slug = str(uuid.uuid4())[:8]
            dicout[slug] = row
            dicout[slug]['worldwide_gross_usd'] = dicout[slug]['worldwide_gross_usd'].replace("$","")

    #
    return dicout

def make_movie(title, length, directory, year):
    return {"title": title, "length": length, "directory": directory, "year": year}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

def abort_if_movie_doesnt_exist(movie_id):
    if movie_id not in MOVIES:
        abort(404, message="Movie {} doesn't exist".format(movie_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# MovieList
# shows a list of all todos, and lets you POST to add new tasks
class MovieList(Resource):
    def get(self):
        return MOVIES

    def post(self):
        args = parser.parse_args()
        slug = str(uuid.uuid4())[:8]
        new_movie = request.get_json()
        pprint.pprint(new_movie)
        MOVIES[slug] = new_movie 
        return MOVIES[slug], 201

# Movie
# shows a single movie item and lets you delete a movie items
class Movie(Resource):
    def get(self, movie_id):
        abort_if_movie_doesnt_exist(movie_id)
        return MOVIES[movie_id]

    def delete(self, movie_id):
        abort_if_movie_doesnt_exist(movie_id)
        del MOVIES[movie_id]
        return '', 204

    def put(self):
        '''
        'ffcb5765': {'audience_score_percent': '55',
                      'film': 'License to Wed',
                      'genre': 'Comedy',
                      'lead_studio': 'Warner Bros.',
                      'profitability': '1.9802064',
                      'rotten_tomatoes_percent': '8',
                      'worldwide_gross_usd': '$69.31 ',
                      'year': '2007'}}
        '''
        new_movie = request.get_json()
        pprint.pprint(new_movie)
        MOVIES[slug] = new_movie 
        return task, 201



##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(MovieList, '/movies')
api.add_resource(Movie, '/movies/<movie_id>')


if __name__ == '__main__':
    MOVIES=initialize_movies()
    #
    app.run(debug=True)
