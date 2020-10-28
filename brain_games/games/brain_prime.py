from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    question = randint(0, 100)
    right = 'yes' if make_prime(question) else 'no'

    return question, right


def make_prime(num):
    number = math.sqrt(num)

    i = 2
    while i <= number:
        if num % i == 0:
            return False
        else:
            i += 1

    return True
