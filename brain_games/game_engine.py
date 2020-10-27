from brain_games.cli import welcome_user, get_answer

MAX_ROUND = 3


def start_game(game):
    player_name = welcome_user()
    print(game.DESCRIPTION)
    round_number = 0
    while round_number < MAX_ROUND:
        ask, right = game.start_game()
        answer = get_answer(ask)
        round_number += 1
        if answer != right:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{right}'.", )
            print(f"Let's try again, {player_name}!")
            break
        else:
            print("Correct")

    print(f"Congratulations, {player_name}!")
