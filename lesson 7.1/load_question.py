from pprint import pprint as pp
import json

questions = {}
points = 0
correct = 0
incorrect = 0
flag = 0


def load_questions():
    with open('question.json', 'r', encoding='UTF-8') as file:
        questions = json.load(file)
    return questions


def show_field():  # Добавить выравнивание
    # Транспорт 100 200 300
    # Животные  100 200 300
    # Еда       100 200 300
    stroka = ''
    category = list(questions.keys())
    max_str = max(category, key=len)
    for i in category:
        stroka = i.ljust(len(max_str))
        for key in questions[i]:
            if questions[i][key]['asked'] == False:
                stroka = stroka + ' ' + key
            else:
                stroka = stroka + ' ' + '   '
        print(stroka)


def parse_input():
    while True:
        user_choose = input("введите категорию и цену")
        category, price = user_choose.capitalize().split()
        if category not in questions:
            print("Такого вопроса нет, попробуйте еще раз")
            continue
        elif price in questions[category] and questions[category][price][
            'asked'] == False:  # добавить проверку на категорию
            questions[category][price]['asked'] = True
            break
        else:
            print("Такого вопроса нет, попробуйте еще раз")

    return category, price


def show_question(category, price):
    ans = input(f"Слово {questions[category][price]['question']} В переводе означает?")
    return ans


def show_stat():
    print(f"У Вас заклончились вопросы\n Ваш Счёт: {points}\nВерных ответов: {correct}\n неверных ответов: {incorrect}")


def save_results_to_file():
    with open('resalt.json', 'a') as file:
        file.write(f"{points}, {correct}, {incorrect}\n")
    return True


questions = load_questions()
category = list(questions.keys())
price = questions[category[0]]
category_quontaty = len(questions)
questions_quontaty = len(price)
for i in range(category_quontaty * questions_quontaty):
    show_field()
    category, price = parse_input()
    ans = show_question(category, price).lower()
    if ans == questions[category][price]["answer"]:
        points += int(price)
        correct += 1
        print(f"\nВерно, +{price}, Ваш счёт = {points}\n")
    else:
        incorrect += 1
        points -= int(price)
        print(f"\nНеверно, на самом деле - {questions[category][price]['answer']},-{price}. Ваш счёт = {points}\n")
show_stat()
save_results_to_file()


