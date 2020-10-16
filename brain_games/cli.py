import prompt


def user_answer(ask):
    print(f"Question: {ask}")
    answer = prompt.string("Your answer: ")
    return answer

def start():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name
