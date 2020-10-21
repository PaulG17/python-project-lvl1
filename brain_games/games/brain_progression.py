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
    correct = progression[skip]
    progression[skip] = ".."
    question = " ".join(progression)

    return (question, correct)
