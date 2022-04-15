from random import randint


GAME_RULES = "Answer 'yes' if the number is even, otherwise answer 'no'."


def generate_question_answer():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    question = ("Question: {}".format(number))
    return question, answer
