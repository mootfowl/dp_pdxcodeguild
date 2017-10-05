'''
Lab 13: Guess the Number

Version 2

Allow the user to make an unlimited number of guesses using a while True and break.
Keep track of how many guesses the user has made, and tell them at the end.

'''

import random

user_guess = int(input("Let's play a game! \nI've picked a random number between 1 and 10. \nCan you guess what it is? > "))
random_selection = random.randint(1, 10)
i = 1

while random_selection != user_guess:
    print("Nope. Try again.")
    user_guess = int(input("Pick a number between 1 and 10. > "))
    i += 1
    if user_guess == random_selection:
        print(f"Good guess, you win! My number was indeed {random_selection}.")
        print(f"And you were able to guess my number in only {i} tries!")


