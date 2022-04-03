import prompt


def run_game(game):
    #welcoming and asking name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    #counditions of a game
    print(game.common_phrase)
    rounds = 3
    counter = 0
    while counter < rounds:
        question, result =                    
        print(question)
        answer = prompt.string("Your answer: ")
        if answer == result:
            print("Correct!")
            counter = counter + 1
        else:
            print(answer + " is wrong answer ;(. Correct answer was " + result + ".")
            print("Let`s try again, " + name + "!")
            break
    print("Congratulations, " + name + "!")
