import requests
from random import shuffle
'''Загрузка случайного слова состороннего ресурса'''

def load_random_word():
    from BasicWord import Basic_word
    req = requests.get("https://jsonkeeper.com/b/UP7W")
    setting = req.json()
    shuffle(setting)

    word = Basic_word(setting[0]["word"], setting[0]["subwords"])

    return word
