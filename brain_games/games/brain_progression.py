from random import randint


DESCRIPTION = "What number is missing in the progression?"


def make_progression():
    step = randint(1, 10)
    start = randint(1, 100)
    stop = start + (step * 10)
    progression = [str(x) for x in range(start, stop, step)]

    return progression


def start_game():
    progression = make_progression()
    skip = randint(0, 9)
    right_answer = progression[skip]
    question = " ".join([
        str(n) if i != skip else ".."
        for i,n in enumerate(progression)])

    return question, right_answer
