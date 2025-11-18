import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # 1. The computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # 2. Get the user's guess
        # We wrap input() in int() to convert the text to a number
        guess = int(input("Make a guess: "))
        attempts += 1

        # 3. Check the logic
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # 4. The user guessed correctly
            print(f"Congratulations! You found the number in {attempts} tries.")
            break  # This stops the loop

# Run the function
start_game()