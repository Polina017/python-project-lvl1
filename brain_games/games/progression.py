import random


GAME_RULES = 'What number is missing in the progression?'


def generate_question_answer():
    progression = generate_progression()
    secret_index = random.randint(0, len(progression) - 1)
    progression = list(map(str, progression))
    symbol = progression[secret_index]
    progression[secret_index] = ".."
    answer = symbol
    question = ("Question: " + " ".join(progression))
    return question, answer


def generate_progression():
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 5)
    number_3 = number_1 + 10 * number_2
    progression = list(range(number_1, number_3, number_2))
    return progression
