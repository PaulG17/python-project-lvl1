from random import randint


condition = 'Answer "yes" if number even otherwise answer "no".'


def run_game():
    question = randint(1, 100)
    if question % 2 == 0:
        bool_right = "yes"
    else:
        bool_right = "no"

    return question, bool_right
