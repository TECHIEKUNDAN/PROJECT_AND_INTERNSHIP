import random

def generate_code(length):
    """Generate a secret code of a given length."""
    return ''.join([str(random.randint(1, 6)) for _ in range(length)])

def get_feedback(secret_code, guess):
    """Provide feedback on the guess compared to the secret code."""
    correct_position = 0
    correct_digit = 0

    secret_code_copy = list(secret_code)
    guess_copy = list(guess)

    # First pass: count correct positions
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_position += 1
            secret_code_copy[i] = '-'
            guess_copy[i] = '-'

    # Second pass: count correct digits (but wrong positions)
    for i in range(len(guess_copy)):
        if guess_copy[i] != '-' and guess_copy[i] in secret_code_copy:
            correct_digit += 1
            secret_code_copy[secret_code_copy.index(guess_copy[i])] = '-'

    return correct_position, correct_digit

def mastermind_game():
    """Play the Mastermind game."""
    print("Welcome to Mastermind!")
    code_length = 4
    secret_code = generate_code(code_length)
    attempts = 10

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: Enter your {code_length}-digit guess (digits 1-6): ")
            if len(guess) == code_length and all(char in '123456' for char in guess):
                break
            print("Invalid guess. Please enter a valid 4-digit code using digits 1-6.")

        correct_position, correct_digit = get_feedback(secret_code, guess)
        print(f"Correct positions: {correct_position}, Correct digits (wrong position): {correct_digit}")

        if correct_position == code_length:
            print(f"Congratulations! You've guessed the code: {secret_code}")
            return

    print(f"Game over! The secret code was: {secret_code}")

# Run the game
mastermind_game()
