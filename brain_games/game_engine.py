from brain_games.cli import welcome_user, user_answer

MAX_ROUND = 3


def start_game(game):
    player_name = welcome_user()
    print(game.DESCRIPTION)
    score = 0
    while score < MAX_ROUND:
        ask, right = game.start_game()
        answer = user_answer(ask)
        score += 1
        if answer != right:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{right}'.", )
            print(f"Let's try again, {player_name}!")
        else:
            print("Correct")

    print(f"Congratulations, {player_name}!")
