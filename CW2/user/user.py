from flask import Blueprint, render_template, request
from utils import get_content, get_posts_by_user
import json

posts_path = 'data/data.json'
comment_path = 'data/comments.json'

user_blueprint = Blueprint('user_blueprint', __name__,
                             template_folder='templates')


@user_blueprint.route('/users/<string:username>', methods=['GET'])
def user_page(username):
    user_posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, len_posts=len(user_posts))
