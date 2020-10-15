import prompt
from brain_games.games.engine import round_number



def calc():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the randomber is even, otherwise answer "no".')

    i = 0
    count = 0
    while i != 3 or count <= round_number:
        count += 1
        first_num = random_num
        second_num = random_num
        action = random_num

        result = 0

        if action < 33:
            random_num = (f"{first_num} + {second_num}")
            result = first_num + second_num
        elif action > 33 and action < 66:
            random_num = (f"{first_num} - {second_num}")
            result = first_num - second_num
        elif action > 66:
            random_num = (f"{first_num} * {second_num}")
            result = first_num * second_num


        print(f"Question: {random_num}")
        yesno = prompt.string("Your answer: ")

        if yesno == result:
            print('Correct!')
            i += 1
        else:
            print(f"'{yesno}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {user_name}")
    print(f'Congratulations, {user_name}!')