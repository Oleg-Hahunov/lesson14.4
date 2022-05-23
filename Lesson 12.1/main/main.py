from flask import Blueprint, render_template, request
import json
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__,
                           template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search', methods=['GET'] )
def page_search():
    """поиск по запросу переданному из формы index.html"""
    s = request.args['s'].lower()
    results = []
    posts = []
    with open("posts.json", 'r', encoding='UTF-8') as file:
        posts = json.load(file)
    for i in range(len(posts)):
        if s in posts[i-1]['content']:
            results.append(posts[i-1])
    return render_template('post_list.html', results=results, len_results=len(results), s=s)
