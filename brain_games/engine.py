import prompt


NUMBER_LEVELS = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name: ")
    print("Hello, {}!".format(name))

    print(game.GAME_RULES)

    for counter in range(NUMBER_LEVELS):
        game_question, right_answer = game.generate_question_answer()
        print(game_question)
        user_answer = prompt.string("Your answer: ")

        if user_answer == right_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, right_answer)) # noqa: 501
            print("Let's try again, {}!".format(name))
            break
    else:
        print("Congratulations, {}!".format(name))
