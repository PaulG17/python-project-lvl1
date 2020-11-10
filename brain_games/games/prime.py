from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    question = randint(0, 100)
    right_answer = 'yes' if is_prime(question) else 'no'

    return question, right_answer


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False
