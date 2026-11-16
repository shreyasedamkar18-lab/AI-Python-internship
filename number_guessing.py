# Number Guessing Game

import random

secret_number = random.randint(1, 20)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("I have selected a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        print("Number of attempts:", attempts)
        break

    elif guess < secret_number:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")