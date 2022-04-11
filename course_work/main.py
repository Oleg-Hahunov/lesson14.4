from BasicWord import Player
from utils import load_random_word

"""основной модуль программы"""

name = input('Здравствуйте\n Введите имя игрока')

User = Player(name)

print(f"привет {User.name}")
Words = load_random_word()
print(f"Надо составить {len(Words.sub_words)} из Слова {Words.main_word} ")
print(f"слова не должны быть короче 4 Букв")  # Добавить оценку длинны слов
print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
print("Поехали, ваше первое слово?")

flag = 0
while len(
        Words.sub_words) > User.user_words_count():  # условия проверки: если список слов пользователя меньше слов - гадаем дальше
    user_word = input("").lower()
    if user_word == 'stop' or user_word == 'стоп':
        break
    if User.user_word_chek(user_word):
        print('такое слово уде было')
        continue
    if Words.user_check(user_word):
        print('верно')
        User.add_user_words(user_word)
        flag += 1
    else:
        print("такого слова я не знаю")

print(f'игра закончена!')
print(f'Вы угадали {flag} слов')
