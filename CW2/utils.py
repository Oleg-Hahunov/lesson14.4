import json

posts_path = 'data/data.json'
comment_path = 'data/comments.json'


def get_content(posts_path):
    """возвращает посты"""
    with open(posts_path, 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя.
    Функция должна вызывать ошибку `ValueError` если такого пользователя нет и
    пустой список, если у пользователя нет постов.
    """
    user_posts = []
    posts = get_content(posts_path)
    for post in posts:
        if user_name == post['poster_name']:
            user_posts.append(post)
    if len(user_posts):
        return user_posts
    raise ValueError('такого пользователя нет.')




def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет и
    пустой список, если у поста нет комментов.
    """
    try:
        comment_list = []
        comments = get_content(comment_path)
        for comment in comments:
            if comment['post_id'] == post_id:
                comment_list.append(comment)
        return comment_list
    except ValueError:
        return f'такого поста нет или у него нет комментариев'




def search_for_posts(query):
    """возвращает список постов по ключевому слову
    """
    post_list=[]
    posts = get_content(posts_path)
    for post in posts:
        if query in post['content']:
            post_list.append(post)
    return post_list



def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору."""
    posts = get_content(posts_path)
    for post in posts:
        if pk == post['pk']:
            return post
    raise ValueError('такого поста')
