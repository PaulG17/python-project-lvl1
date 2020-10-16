from operator import add, mul, sub
from random import randint, choice


result = "What is the result of the expression?"
operator = [("+", add), ("*", mul), ("-", sub)]


def start_game():
    one = randint(1, 100)
    two = randint(1, 100)
    action, function = choice(operator)
    ask = f"{one} {action} {two}"
    right = function(one, two)
    return (ask, str(right))
