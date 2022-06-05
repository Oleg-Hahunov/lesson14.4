from flask import Flask, render_template, jsonify

from search.search import search_blueprint
from user.user import user_blueprint
from utils import get_content, get_post_by_pk, get_comments_by_post_id
import logging

logging.basicConfig(filename='logs/api.log', level=logging.INFO)  # логирование ошибок
posts_path = 'data/data.json' #расположение файла с постами
comment_path = 'data/comments.json' #расположение файла с комментами

app = Flask(__name__)


@app.route('/')
def posts_index():
    """основная страничка"""
    posts = get_content(posts_path)
    return render_template('index.html', posts=posts, posts_len=len(posts))


@app.route('/post/<int:post_pk>')
def the_post(post_pk):
    """отдельный пост с комментариями"""
    post = get_post_by_pk(post_pk)
    comments = get_comments_by_post_id(post_pk)
    return render_template('post.html', post=post, comments=comments, comments_len=len(comments))


"""обработка ошибок"""


@app.errorhandler(404)
def pageNot(error):
    return ("такой страницы не существует", 404)


@app.errorhandler(505)
def pageNot(error):
    return ("сервер не ответил во время", 505)


app.register_blueprint(search_blueprint) #Блюпринт поиска по словам
app.register_blueprint(user_blueprint) #Блюпринт вывода всех постов конкретного пользователя

""""""


@app.route('/api/posts', methods=['GET'])
def read_posts():
    posts = get_content(posts_path)
    return jsonify(posts)


@app.route('/api/posts/<int:post_pk>', methods=['GET'])
def read_one_post(post_pk):
    logging.info(f" /api/posts/{post_pk}")
    post = get_post_by_pk(post_pk)
    return jsonify(post)


app.run()
