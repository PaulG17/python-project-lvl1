from brain_games.cli import welcome_user, user_answer


max_round = 3
def start_game(input):
    player_name = welcome_user(input.condition)
    score = 0
    while score < max_round:
        ask, right = input.start_game()
        answer = user_answer(ask)
        if answer != right:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{right}'.",
            )
            print(f"Let's try again, {player_name}!")
            return
        print("Correct")
        score += 1
    print(f"Congratulations, {player_name}!")
