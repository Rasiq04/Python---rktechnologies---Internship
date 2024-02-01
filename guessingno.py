import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Allow the player 10 attempts to guess the number
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        # try:
        #     # Get the player's guess
        guess = int(input("Enter your guess: "))
        # except ValueError:
        #     print("Please enter a valid number.")
        #     continue

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts + 1} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

        attempts += 1

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
guess_the_number()
