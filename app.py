from flask import Flask, jsonify

from steps_5_6 import films_by_query
from utils import *

app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route("/movie/<title>")
def searh_films(title):
    data = search_films(title)
    return jsonify(data)

@app.route("/movie/<int:year_1>/to/<int:year_2>")
def search_years(year_1, year_2):
    data = search_by_years(year_1, year_2)
    return jsonify(data)

@app.route("/rating/<rating>")
def search_rating(rating):
    my_dict = {
        "children": "rating = 'G'",
        "family": "rating = 'G' or rating = 'PG' or rating = 'PG-13'",
        "adult": "rating = 'R' or rating = 'NC-17'"
    }
    query = f"SELECT title, rating, description FROM netflix where {my_dict[rating]}"
    data = search_by_rating(query=query)
    return jsonify(data)

@app.route("/genre/<genre>")
def search_fresh_films(genre):
    data = fresh_films(genre)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
