import csv
import uuid
import pprint

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
from flask_apispec import use_kwargs, marshal_with 
from flask_apispec.views import MethodResource
from flask_apispec.extension import FlaskApiSpec 
from marshmallow import Schema, fields
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from api_utils import initialize_movies


def make_movie(title, length, directory, year):
    return {"title": title, "length": length, "directory": directory, "year": year}


def abort_if_movie_doesnt_exist(movie_id):
    if movie_id not in MOVIES:
        abort(404, message="Movie {} doesn't exist".format(movie_id))

class MovieSchema(Schema):
    class Meta:
        fields = ('film', 'genre', 'lead_studio', 'audience_score_percent', 'profitability', 'rotten_tomatoes_percent', 'worldwide_gross_usd', 'year')

# MovieListResource
# shows a list of all movies, and lets you POST to add new tasks
class MovieListResource(MethodResource):
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

# MovieResource
# shows a single movie item and lets you delete a movie items
class MovieResource(MethodResource):
    @marshal_with(MovieSchema)
    def get(self, movie_id):
        abort_if_movie_doesnt_exist(movie_id)
        return MOVIES[movie_id]

    @marshal_with(None, code=204)
    def delete(self, movie_id):
        abort_if_movie_doesnt_exist(movie_id)
        del MOVIES[movie_id]
        return '', 204

    @use_kwargs(MovieSchema)
    @marshal_with(MovieSchema)
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
    #
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='Backend for Redux Testing',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
    })
    docs = FlaskApiSpec(app)
    #
    api.add_resource(MovieListResource, '/movies')
    api.add_resource(MovieResource, '/movies/<movie_id>')
    ##
    docs.register(MovieListResource)
    docs.register(MovieResource)
    ##
    app.run(debug=True)


if __name__ == '__main__':
    #
    MOVIES=initialize_movies()
    main()
