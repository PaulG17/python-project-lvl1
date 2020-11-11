import prompt

MAX_ROUND = 3


def start_game(game=None):
    print("Welcome to the Brain Games!")

    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    if game is not None:
        print(game.DESCRIPTION)
        round_number = 0
        while round_number < MAX_ROUND:
            question, right_answer = game.prepare_round()
            print(f"Question: {question}")
            answer = prompt.string("Your answer: ")
            round_number += 1
            if answer != right_answer:
                print(f"'{answer}' is wrong answer ;(.",
                      f"Correct answer was '{right_answer}'.", )
                print(f"Let's try again, {user_name}!")
                return
            else:
                print("Correct")

        print(f"Congratulations, {user_name}!")
