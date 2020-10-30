from brain_games.cli import welcome_user, get_answer

MAX_ROUND = 3


def start_game(game):
    player_name = welcome_user()
    print(game.DESCRIPTION)
    round_number = 0
    error = 0
    while round_number < MAX_ROUND:
        question, right_answer = game.start_game()
        answer = get_answer(question)
        round_number += 1
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{right_answer}'.", )
            print(f"Let's try again, {player_name}!")
            error = 1
            break
        else:
            print("Correct")

    if error == 0:
        print(f"Congratulations, {player_name}!")
