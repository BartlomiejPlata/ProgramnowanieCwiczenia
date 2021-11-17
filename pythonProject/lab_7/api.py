from flask import Flask
from flask_restful import Resource, Api
from lab_7.Movie import Movie
import json

app = Flask(__name__)
api = Api(app)

def read_file(filename) ->str:
    file = open(filename, encoding="utf8")
    content = file.readlines()
    return content


class HelloWorld(Resource):
    def get(self):
        m1 = Movie(1, "tytuł filmu", "Familijny")
        data = read_file('C:/Users/Hp/ProgramnowanieCwiczenia/pythonProject/lab_7/movies.csv')
        movies = list()
        for x in data:
            movies.append(Movie(x.split(',')[0],x.split(',')[1],x.split(',')[2]).__dict__)
        return movies







api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

