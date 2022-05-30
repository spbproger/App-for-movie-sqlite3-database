
from flask import Flask, jsonify

from utilities import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

@app.route('/movie/<title>')
def get_movie_by_title(title):
    return movie_by_title(title)


@app.route('/movie/<int: year>/to/<int: year>')
def get_movie_by_year(year1, year2):
    return jsonify(movies_between_years(year1, year2))


@app.route('/rating/<str: category>')
def get_movie_by_rating(category):
    return jsonify(movies_by_rating(category))

if __name__ == "__main__":
    app.run(debug=True)