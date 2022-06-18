from flask import Flask, jsonify
from utils import search_by_name, search_by_years, search_by_rating, search_by_listed_in, acter_list, search_by_list

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
def search(title):
    return jsonify(search_by_name(title))


@app.route('/movie/<int:year1>/to/<int:year2>')
def search_by_year(year1, year2):
    return jsonify(search_by_years(year1, year2))


@app.route('/rating/<lvl>')
def search_by_lvl(lvl):
    return jsonify(search_by_rating(lvl))


@app.route('/genre/<genre>')
def search_by_genre(genre):
    return jsonify(search_by_listed_in(genre))

@app.route('/search/<tipe>/<genre>/<int:year>')
def search_by_(tipe, genre, year):
    return jsonify(search_by_list(tipe, genre, year))




app.run()
