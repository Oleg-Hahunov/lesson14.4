from flask import Blueprint, render_template, request
from utils import get_content, search_for_posts
import json

posts_path = 'data/data.json'
comment_path = 'data/comments.json'

search_blueprint = Blueprint('search_blueprint', __name__,
                             template_folder='templates')


@search_blueprint.route('/search', methods=['GET'])
def page_search():
    """Блюпринт поиска по словам"""
    s = request.args['s'].lower()
    posts = []
    posts_ = get_content(posts_path)
    for i in range(len(posts_)):
        if s in posts_[i]['content']:
            posts.append(posts_[i])
    return render_template('search.html', posts=posts, len_posts=len(posts), s=s)
