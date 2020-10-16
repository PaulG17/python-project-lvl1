from random import randint


RULES = 'Answer "yes" if number even otherwise answer "no".'


def start_game():
    question = randint(1, 100)
    if question % 2 == 0:
        bool_right = "yes"
    else:
        bool_right = "no"
    return (ask, bool_right)
