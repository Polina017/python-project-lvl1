from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def generate_question_answer():
    number_1 = randint(10, 20)
    number_2 = randint(1, 10)
    operator = choice("+-*")
    question = ("Question: {} {} {}".format(number_1, operator, number_2))
    if operator == "+":
        answer = number_1 + number_2
    elif operator == "-":
        answer = number_1 - number_2
    elif operator == "*":
        answer = number_1 * number_2
    answer = str(answer)
    return question, answer
