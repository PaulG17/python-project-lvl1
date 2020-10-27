from operator import add, mul, sub
from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def start_game():
    one = randint(1, 100)
    two = randint(1, 100)
    operator = [("+", add), ("*", mul), ("-", sub)]
    action, function = choice(operator)
    answer = f"{one} {action} {two}"
    right_answer = function(one, two)

    return answer, str(right_answer)
