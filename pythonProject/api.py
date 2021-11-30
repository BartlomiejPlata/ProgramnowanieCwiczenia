from flask import Flask
from flask_restful import Resource, Api
from lab_7.Links import Link
from lab_7.Movie import Movie

from lab_7.Ratings import Rating
from lab_7.Tag import Tag

app = Flask(__name__)
api = Api(app)

def read_file(filename) ->str:
    file = open(filename, encoding="utf8")
    content = file.read().splitlines()
    return content


class moviePage(Resource):
    def get(self):
        data = read_file('/lab_7/movies.csv')
        movies = list()
        for x in data:
            movies.append(Movie(x.split(',')[0],x.split(',')[1],x.split(',')[2]).__dict__)
        return movies

class LinksPage(Resource):
    def get(self):
        data = read_file('lab_7/links.csv')
        links = list()
        for x in data:
            links.append(Link(x.split(',')[0],x.split(',')[1],x.split(',')[2]).__dict__)
        return links


class RatingsPage(Resource):
    def get(self):
        data = read_file('/lab_7/ratings.csv')
        ratings = list()
        for x in data:
            ratings.append(Rating(x.split(',')[0],x.split(',')[1],x.split(',')[2],x.split(',')[3]).__dict__)
        return ratings


class TagsPage(Resource):
    def get(self):
        data = read_file('/lab_7/tags.csv')
        tags = list()
        for x in data:
            tags.append(Tag(x.split(',')[0],x.split(',')[1],x.split(',')[2],x.split(',')[3]).__dict__)
        return tags




api.add_resource(moviePage, '/movies')
api.add_resource(LinksPage, '/links')
api.add_resource(RatingsPage, '/ratings')
api.add_resource(TagsPage, '/tags')

if __name__ == '__main__':
    app.run(debug=True)

