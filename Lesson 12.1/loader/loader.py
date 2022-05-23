from flask import Blueprint, render_template, request
import json
import logging
from loader.utils import picture_save, post_added

logging.basicConfig(filename='log_ex.txt', level=logging.INFO)  # логирование ошибок
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def post_loader():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_creater():
    picture = request.files.get('picture')
    content = request.form.get('content')
    posts = []
    post = {'pic': picture_save(picture), 'content': content}
    if not picture or not content:
        return f"не все поля заполнены"
    try:
        with open("posts.json", 'r', encoding='UTF-8') as file:
            posts = json.load(file)
    except FileNotFoundError:
        logging.exception('не найден json файл')
        return f'фаил с постами не найден'

    posts.append(post)
    post_added(posts)

    return render_template('post_uploaded.html', post=post)
