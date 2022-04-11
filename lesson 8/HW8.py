import json


class Question():
    def __init__(self, TextQuestion, LvlQuestion, Ans):
        self.TextQuestion = TextQuestion
        self.LvlQuestion = LvlQuestion
        self.Ans = Ans
        # self.stat = Statquestion
        # self.userAns = UserAns

    def get_points(self):  # возвращает количество баллов за ответ. (int)
        return int(self.LvlQuestion) * 10

    def is_correct(self, userAns):  # проверяет ответ пользователя
        self.userAns = userAns
        if self.Ans == self.userAns:
            return True  #
        return False  #

    def build_question(self):  # формирует текст вопроса для пользователя
        return f"Вопрос: {self.TextQuestion}\nСложность: {self.LvlQuestion}/5"

    def correct(self):  # результат при правильном ответе
        print(f"Ответ верный, получено {int(self.LvlQuestion) * 10} баллов")

    def uncorrect(self):  # результат при неправильном ответе
        print(f"Ответ неверный, верный ответ {self.Ans}")



def load_questions():
    with open('questions.json', 'r') as File:
        questions = json.load(File)
    return questions

def resalt(flag=0, score=0):  # подсчёт итоговых результатов
    for que in questions:
        if int(que["ua"]) > 0:
            flag += 1
            score += int(que["ua"])
    print(f"Вот и всё!\nОтвечено {flag} вопроса из {len(questions)}\nНабрано баллов: {score}")

questions = load_questions()
from random import shuffle

for i in range(len(questions)):  # тело программы
    while True:  # сперва не понял какое количество вопросов будет, по этому создал цикл проверки "был ли такой вопрос?".
        # если обязательно проходить все вопросы, тогда достаточно оставить протсо shuffle
        shuffle(questions)
        if questions[0]["sq"] == False:
            questions[0]["sq"] = True
            break
    question = Question(questions[0]["q"], questions[0]["d"], questions[0]["a"])

    print(question.build_question())
    if question.is_correct(userAns=input().capitalize()) == True:  # проверка ответа и внесение данных в словарь
        question.correct()
        questions[0]["ua"] = int(questions[0]["d"]) * 10
    else:
        question.uncorrect()
        questions[0]["ua"] = 0

resalt()
