from flask import Blueprint, render_template, request
import json
import logging

logging.basicConfig(filename='log_ex.txt', level=logging.INFO) #логирование ошибок
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def post_loader():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_creater():
    try:
        picture = request.files.get('picture')
    except:
        logging.exception('неправильный формат картинки')
        return f'загрузите JPEG файл'
    content = request.form.get('content')
    if not picture or not content:
        return f"не все поля заполнены"
    picture.save(f'uploads/images/{picture.filename}')
    posts = []
    post = {'pic': f'uploads/images/{picture.filename}', 'content': content}
    try:
        with open("posts.json", 'r', encoding='UTF-8') as file:
            posts = json.load(file)
    except FileNotFoundError:
        logging.exception('не найден json файл')
        return f'фаил с постами не найден'

    posts.append(post)
    try:
        with open('posts.json', 'w', encoding='UTF-8') as file:
            json.dump(posts, file, ensure_ascii=False)
    except FileNotFoundError:
        logging.exception('не найден json файл')
        return f'фаил с постами не найден'

    return render_template('post_uploaded.html', post=post)
