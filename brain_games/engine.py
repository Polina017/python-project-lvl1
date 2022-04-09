import prompt


number_levels = 3
incorrect = "is wrong answer ;(. Correct answer was"


def start(module):
    # Greet and asking name of user
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name: ")
    print("Hello, {}!".format(name))
    module.welcome()
    # 3 levels of the game
    count = 1
    while count <= number_levels:
        basic_elements = module.game_logic()
        # result = (question, answer) -> basic_elements = (question, answer)
        (game_question, right_answer) = basic_elements
        print(game_question)
        user_answer = prompt.string("Your answer: ")
        if user_answer == right_answer:
            print("Correct!")
            count += 1
        else:
            print("'{}' {} '{}'.".format(user_answer, incorrect, right_answer)) # noqa: 501
            print("Let's try again, {}!".format(name))
            break
    # If user passed 3 levels, he won
    else:
        print("Congratulations, {}!".format(name))
