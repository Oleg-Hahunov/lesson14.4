name = input('Привет. \n Как Вас зовут? \n')

count = 0
filename = 'words.txt'
words = []
history = 'history.txt'
data = []
ans = ''


def read_words(filename):  # модуль считывания слов из файла. возвращает массив из слов
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip('\n'))
    return words


def add_top(name, count):  # модуль внесения результата в хистори
    with open('history.txt', 'a') as file:
        file.write(f'{name} {count}\n')


def read_top():  # вывод результата
    import re
    flag = 0
    max_lvl = 0
    resalt = []
    with open('history.txt') as file:
        history_list = file.read().splitlines()
        for line in history_list:
            flag += 1
            resalt = re.split(r' ', str(line))
            if int(resalt[1]) > int(max_lvl):
                max_lvl = resalt[1]
    print(f' Всего сыграно игр: {flag} \n Максимальный рекорд {max_lvl}')


data = read_words(filename)
from random import sample

for i in data:
    ans = input(f'Угадайте слово {"".join(sample((i), k=len(i)))}\n')
    if ans.lower() == i:
        print('Верно, Вы получаете 10 очков')
        count += 10
    else:
        print(f'неверно, Верный ответ - {i}')

add_top(name, count)
read_top()

