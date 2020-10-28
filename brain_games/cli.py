import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    return user_name


def get_answer(ask):
    print(f"Question: {ask}")
    answer = prompt.string("Your answer: ")

    return answer
