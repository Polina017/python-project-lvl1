from random import randint

common_phrase = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    n = randint(0, 50)
    question = 'Question: ', n
    if n % 2 == 0:
        answer = "yes"
    elif n % 2 == 1:
        answer = "no"
    return question, answer
