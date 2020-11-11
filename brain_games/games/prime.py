from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prepare_round():
    question = randint(0, 100)
    right_answer = 'yes' if is_prime(question) else 'no'

    return question, right_answer


def is_prime(num):
    if num < 2:
        return False

    for devider in range(2, num):
        if num % devider == 0:
            return False

    return True
