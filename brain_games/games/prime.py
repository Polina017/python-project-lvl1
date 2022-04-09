import random
import math


def welcome():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game_logic():
    num = random.randint(1, 100)
    if num % 2 == 0 and num == 2:
        answer = "yes"
    elif num % 2 == 0 and num != 2:
        answer = "no"
    count = 0
    for count in range(3, round(math.sqrt(num))):
        if num % count == 0:
            count += 1
    if count <= 0:
        answer = "yes"
    else:
        answer = "no"
    question = ("Question: {}".format(num))
    result = (question, answer)
    return result
