import random

def guessing_game():
    number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

guessing_game()