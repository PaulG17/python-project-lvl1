from random import randint


DESCRIPTION = "What number is missing in the progression?"


def make_progression(length):
    step = randint(1, 10)
    start = randint(1, 100)
    stop = start + (step * length)
    progression = [str(x) for x in range(start, stop, step)]

    return progression


def prepare_round():
    length = 10
    progression = make_progression(length)
    missing_element_index = randint(0, length-1)
    right_answer = progression[missing_element_index]
    question = " ".join([
        str(n) if i != missing_element_index else ".."
        for i, n in enumerate(progression)])

    return question, right_answer
