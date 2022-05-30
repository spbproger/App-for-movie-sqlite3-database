
import json
from flask import Flask
from utilities import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
def get_by_movie_title(title):
    return get_by_title(title)


if __name__ == "__main__":
    app.run(debug=True)