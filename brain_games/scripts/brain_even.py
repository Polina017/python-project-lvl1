#!/usr/bin/env python
import prompt
from random import randint

def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def checking_for_even(): # noqa: 901
    i = 1
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 4:
        r = randint(0, 50)
        print('Question: ', r)
        answer = prompt.string('Your answer: ')
        if (r % 2 == 0 and answer == "yes"):
            print('Correct!')
        elif (r % 2 == 0 and answer == "no"):
            print('"no" is wrong answer ;(. Correct answer was "yes".')
            print('Lets`s try again, ' + name + '!')
            break
        elif (r % 2 == 1 and answer == "no"):
            print('Correct!')
        elif (r % 2 == 1 and answer == "yes"):
            print('"yes" is wrong answer ;(. Correct answer was "no".')
            print('Lets`s try again, ' + name + '!')
            break
        if i == 3:
            print('Congratulations, ' + name + '!')
        i = i + 1


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    checking_for_even()


if __name__ == '__main__':
    main()
