import random

# Generate a random number between 1 and 10
random_num = random.randint(1, 10)

# Get user input
guess = input("Enter a number between 1 and 10: ")

# Check if input is a valid integer
if guess.isdigit():
    guess = int(guess)
    if guess == random_num:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, the correct number was {random_num}.")
else:
    print("Invalid input! Please enter a number between 1 and 10.")

