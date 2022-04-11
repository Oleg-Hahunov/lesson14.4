class Basic_word:  # клаас получает основное словов и варианты которые можно из него составить

    def __init__(self, main_word, sub_words):
        self.main_word = main_word
        self.sub_words = sub_words

    def user_check(self, user_word):  # проверяет есть слово введёное пользоватетем в возможных вариантах.
        return user_word in self.sub_words

    def sub_words_count(self):  # возвращает количество возможных вариантов
        return len(self.sub_words)


class Player:

    def __init__(self, user_name, user_words=None):  # получает имя пользовотеля и слова введёные им
        if user_words is None:
            user_words = []
        self.name = user_name
        self.user_words = user_words

    def user_words_count(self): # количество угаданных слов
        return len(self.user_words)

    def add_user_words(self, user_word): # добавление нового угаданного слова к предыдущим
        self.user_words.append(user_word)

    def user_word_chek(self, user_word): # проверка встречалось ли введённое слово раньше
        return user_word in self.user_words

