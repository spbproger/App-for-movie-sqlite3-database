
from flask import Flask
from utilities import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
def get_by_title(title):
    return movie_by_title(title)


@app.route('//movie/<int: year>/to/<int: year>')
def get_by_year(year1, year2):
    return movies_by_years(year1, year2)


if __name__ == "__main__":
    app.run(debug=True)