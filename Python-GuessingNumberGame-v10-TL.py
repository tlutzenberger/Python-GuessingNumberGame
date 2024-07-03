################################ 
# Tom Lutzenberger
# Date: 03/21/2024
# Python-GuessingNumberGame-v10.py
# Version 1.0
# Description - A simple guessing game for a number between 1-10. The game will continue to loop
# until the user exits.
################################

# import library functions to use
import random

def main():
    num_attempts = 0
    random_number = random.randint(1, 10)

    #Loop for random number guessing
    while True:
        num_attempts += 1
        print("Guess a number between 1 and 10 (or enter 0 to quit):")
        user_guess = input().strip()

        if user_guess == '0':
            print("Exiting the game.")
            break

        if not user_guess.isdigit() or not 1 <= int(user_guess) <= 10:
            print("Invalid input. Please guess a number between 1 and 10.")
            continue

        user_guess = int(user_guess)

        if user_guess < random_number:
            print("Too low. Try again.")
        elif user_guess > random_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly.")
            print(f"You made {num_attempts} attempts.")
            break

if __name__ == "__main__":
    main()
