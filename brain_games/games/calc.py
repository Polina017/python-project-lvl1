from random import randint, choice


def welcome():
    print('What is the result of the expression?')


def game_logic():
    n1 = randint(10, 20)
    n2 = randint(1, 10)
    o = choice("+-*")
    question = ("Question: {} {} {}".format(n1, o, n2))
    if o == "+":
        answer = n1 + n2
    elif o == "-":
        answer = n1 - n2
    elif o == "*":
        answer = n1 * n2
    answer = str(answer)
    result = (question, answer)
    return result
