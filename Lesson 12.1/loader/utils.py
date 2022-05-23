from flask import request
import json
import logging


def picture_save(picture):
    """сохранение картинки"""
    picture = request.files.get('picture')
    picture_name = picture.filename.split('.')[-1]
    if picture_name != 'jpeg' or picture_name != 'png':
        return f'неправильный формат картинки'
    picture.save(f'uploads/images/{picture.filename}')
    return f'uploads/images/{picture.filename}'


def post_added(posts):
    """перезапись нового джейсон файла с добавленным постом"""
    try:
        with open('posts.json', 'w', encoding='UTF-8') as file:
            return json.dump(posts, file, ensure_ascii=False)
    except FileNotFoundError:
        logging.exception('не найден json файл')
        return f'фаил с постами не найден'
