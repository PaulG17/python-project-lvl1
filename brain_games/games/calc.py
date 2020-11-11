from operator import add, mul, sub
from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def prepare_round():
    one = randint(1, 100)
    two = randint(1, 100)
    operations = [("+", add), ("*", mul), ("-", sub)]
    sign, operation = choice(operations)
    question = f"{one} {sign} {two}"
    right_answer = operation(one, two)

    return question, str(right_answer)
