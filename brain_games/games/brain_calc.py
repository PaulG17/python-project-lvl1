from operator import add, mul, sub
from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def start_game():
    one = randint(1, 100)
    two = randint(1, 100)
    operator_list = [("+", add), ("*", mul), ("-", sub)]
    action, function = choice(operator_list)
    question = f"{one} {action} {two}"
    right_answer = function(one, two)

    return question, str(right_answer)
