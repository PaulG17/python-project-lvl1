import prompt
import random
from brain_games.games.engine import round_number


def calc():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('What is the result of the expression?')

    i = 0
    count = 0
    while i != 3 or count < round_number:
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        random_three = random.randint(1, 100)

        count += 0
        result = 0

        if random_three < 33:
            random_num = (f"{first_num} + {second_num}")
            result = first_num + second_num
        elif random_three > 33 and random_three < 66:
            random_num = (f"{first_num} - {second_num}")
            result = first_num - second_num
        elif random_three > 66:
            random_num = (f"{first_num} * {second_num}")
            result = first_num * second_num

        print(f"Question: {random_num}")
        answer = int(prompt.string("Your answer: "))

        if answer == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {user_name}")
    print(f'Congratulations, {user_name}!')