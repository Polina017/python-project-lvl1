from random import randint


GAME_RULES = "Find the greatest common divisor of diven numbers."


def generate_question_answer():
    number_1 = randint(1, 30)
    number_2 = randint(30, 60)
    question = ("Question: {} {}".format(number_1, number_2))
    answer = str(gcd(number_1, number_2))
    return question, answer


def gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_2
