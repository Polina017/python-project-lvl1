from random import randint


def welcome():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def game_logic():
    num = randint(1, 100)
    if num % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    question = ("Question: {}".format(num))
    result = (question, answer)
    return result
