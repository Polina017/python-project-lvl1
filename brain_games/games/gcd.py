from random import randint
import math


def welcome():
    print("Find the greatest common divisor of diven numbers.")


def game_logic():
    n1 = randint(1, 30)
    n2 = randint(30, 60)
    question = ("Question: {} {}".format(n1, n2))
    answer = math.gcd(n1, n2)
    answer = str(answer)
    result = (question, answer)
    return result
