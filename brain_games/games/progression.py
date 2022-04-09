import random


def welcome():
    print('What number is missing in the progression?')


def game_logic():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 5)
    num = num1
    progression = str(num1)
    count = 0
    while count < 9:
        num = num + num2
        progression = progression + " " + str(num)
        count += 1
    last = progression[-2:]
    symbol = random.randrange(num1, int(last), num2)
    change = progression.replace(str(symbol), "..")
    answer = symbol
    answer = str(answer)
    question = ("Question: {}".format(change))
    result = (question, answer)
    return result
