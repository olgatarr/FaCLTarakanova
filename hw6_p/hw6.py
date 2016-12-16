import random

def choice(name):
    f = open(name +'.txt', 'r', encoding='utf-8')
    choice = f.read()
    сhoice = choice.strip()
    choice = choice.split()
    print(choice)
    f.close()
    return random.choice(choice)

def punctuation():
    # эта функция возвращает случайный знак препинания из небольшого списка; у неё нет аргументов
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def make_text():
    first = choice('names') + ' ' + choice('verb_part') + punctuation() + '\n'
    second = 'hän ' + choice('verb_part') + ' ' +choice('noun_part') + punctuation() + '\n'
    third = 'hän ' + choice('verb_gen') + ' ' + choice('noun_gen') + punctuation()
    return first.capitalize() + second.capitalize() + third.capitalize()

print(make_text())
