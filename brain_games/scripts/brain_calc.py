#!/usr/bin/env python
import prompt
import brain_games.scripts.brain_even
from brain_games.scripts.brain_even import welcome_user
from random import randint, choice


def calc(): # noqa: 901
    i = 1
    print('What is the result of the expression?')
    while i < 4:
        n1 = randint(10, 20)
        n2 = randint(1, 10)
        a = n1 + n2
        b = n1 - n2
        c = n1 * n2
        string = [a, b, c]
        o = choice(string)
        if o == a:
            print('Question: ', n1, "+", n2)
        elif o == b:
            print('Question: ', n1, "-", n2)
        elif o == c:
            print('Question: ', n1, "*", n2)
        answer = prompt.string('Your answer: ')
        if int(answer) == a:
            print('Correct!')
        elif int(answer) == b:
            print('Correct!')
        elif int(answer) == c:
            print('Correct!')
        elif (int(answer) != a and o == a):
            print(answer + ' is wrong answer ;(. Correct answer was ' + str(a) + '.') # noqa: 501
            print('Let`s try again, ' + brain_games.scripts.brain_even.name + '!') # noqa: 501
            break
        elif (int(answer) != b and o == b):
            print(answer + ' is wrong answer ;(. Correct answer was ' + str(b) + '.') # noqa: 501
            print('Let`s try again, ' + brain_games.scripts.brain_even.name + '!') # noqa: 501
            break
        elif (int(answer) != c and o == c):
            print(answer + ' is wrong answer ;(. Correct answer was ' + str(c) + '.') # noqa: 501
            print('Let`s try again, ' + brain_games.scripts.brain_even.name + '!') # noqa: 501
            break
        if i == 3:
            print('Congratulations, ' + brain_games.scripts.brain_even.name + '!') # noqa: 501
        i = i + 1


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    calc()


if __name__ == '__main__':
    main()
