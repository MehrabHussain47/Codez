import random # python's Built-In library random

# Generate a random number between 1 to 100
number = random.randint(1, 100)

# print(number)
print("Welcome to the Number Guessing Game!")
print("I've picked a number between 1 to 100. Try to guess it!")

while (True):
    # Take user input
    guess = int(input("Enter your guess: "))

    # Check the guess
    if guess < number:
        print("Too low! Try again")
    elif guess > number:
        print("Too high! try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")
        break   # End the game