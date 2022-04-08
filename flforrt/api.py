import csv
import uuid
import pprint

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource

from api_utils import initialize_movies


def make_movie(title, length, directory, year):
    return {"title": title, "length": length, "directory": directory, "year": year}


def abort_if_movie_doesnt_exist(movie_id):
    if movie_id not in MOVIES:
        abort(404, message="Movie {} doesn't exist".format(movie_id))

# MovieList
# shows a list of all movies, and lets you POST to add new tasks
class MovieList(Resource):
    def get(self):
        return MOVIES

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task')
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


def main():
    #
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    ##
    api.add_resource(MovieList, '/movies')
    api.add_resource(Movie, '/movies/<movie_id>')
    ##
    app.run(debug=True)


if __name__ == '__main__':
    #
    MOVIES=initialize_movies()
    main()
