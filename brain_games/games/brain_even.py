from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def start_game():
    question = randint(1, 100)
    if question % 2 == 0:
        right = "yes"
    else:
        right = "no"

    return question, right
