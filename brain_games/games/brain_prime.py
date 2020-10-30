from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    question = randint(0, 100)
    right_answer = 'yes' if is_prime(question) else 'no'

    return question, right_answer


def is_prime(num):
    sqrt_value = math.sqrt(num)

    i = 2
    while i <= sqrt_value:
        if num % i == 0:
            return False
        else:
            i += 1

    return True
