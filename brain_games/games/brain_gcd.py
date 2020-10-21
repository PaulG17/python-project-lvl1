from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."

def start_game():
    one = randint(1, 100)
    two = randint(1, 100)
    question = f"{one} {two}"
    correct = get_gcd(one, two)

    return (question, str(correct))


def get_gcd(one, two):
    if one == two:
        return one
    if one < two:
        two, one = one, two
    remainder = one % two
    if remainder == 0:
        return two
    while remainder != 0:
        remainder = one % two
        one, two = two, remainder

    return one
