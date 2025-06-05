import random # python's Built-In library random

# Generate a random number between 1 to 100
secret_number = random.randint(1, 100)

# print(secret_number)
print("Welcome to the Number Guessing Game!")
print("I've picked a number between 1 to 100. Try to guess it!")

while (True):
    # Take user input
    guess = int(input("Enter your guess: "))

    # Check the guess
    if guess < secret_number:
        print("Too low! Try again")
    elif guess > secret_number:
        print("Too high! try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly!")
        break   # End the game