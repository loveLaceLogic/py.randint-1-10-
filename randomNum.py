# This program generates a random number between 1 and 10, asks the user to guess the number, and then prints the random number.
import random

randomNum = random.randint(1,10)

print ('Enter a number between 1 and 10:')
guess = input()

randomNum = str(randomNum)
print ('The number is ' + randomNum)