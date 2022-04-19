import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = random.randint(1, 101)
    question = ("Question: {}".format(number))
    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"
    return question, answer


def is_prime(number):
    x = 2
    while x <= number:
        if number == 1 or number == 2:
            return True
        elif x == number:
            return True
        elif number % x != 0:
            x += 1
        else:
            return False
    return True
