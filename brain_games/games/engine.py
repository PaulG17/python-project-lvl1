import random


def round_number():
    round_number = 3
    return round_number

def random_num():
    random_num = random.randint(1, 100)
    return random_num

    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")