from random import randint, choice

common_phrase = 'What is the result of the expression?'


def game_info():
    n1 = randint(10, 20)
    n2 = randint(1, 10)
    a = n1 + n2
    b = n1 - n2
    c = n1 * n2
    string = [a, b, c]
    o = choice(string)


def game_questions():
    o == a or o == b or o == c
    question = 'Question: ', n1, '+'/'-'/'*', n2
    answer = a or answer = b or answer = c
    result = (question, answer)
    return result

