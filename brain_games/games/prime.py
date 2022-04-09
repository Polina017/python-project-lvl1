import random
import math


def welcome():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game_logic():
    num = random.randint(1, 101)
    question = ("Question: {}".format(num))
    x = 2
    while x <= num:
        if num == 1 or num == 2:
            answer = "yes"
            break
        elif x == num:
            answer = "yes"
            break
        elif num % x != 0:
            x += 1
        else:
            answer = "no"
            break
    result = (question, answer)
    return result
