import random
import prompt


def YesNo():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the randomber is even, otherwise answer "no".')

    i = 0
    while i != 3:
        random_num = random.randint(1, 100)
        print(f"Question: {random_num}")
        yesno = prompt.string("Your answer: ")
        if random_num % 2 == 0:
            yesno_real = "yes"
        else:
            yesno_real = "no"
        if yesno == yesno_real:
            print('Correct!')
            i += 1
        else:
            print(f"'{yesno}' is wrong answer ;(. "
                  f"Correct answer was '{yesno_real}'.")
            print(f"Let's try again, {user_name}")
    print(f'Congratulations, {user_name}!')
