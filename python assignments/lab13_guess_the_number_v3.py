'''
Lab 13: Guess the Number

Version 3

Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''

import random

user_guess = int(input("Let's play a game! \nI've picked a random number between 1 and 10. \nCan you guess what it is? > "))
random_selection = random.randint(1, 10)
i = 1

while random_selection != user_guess:
    if user_guess < random_selection:
        print("Your guess is too low!")
        user_guess = int(input("Pick a number between 1 and 10. > "))
        i += 1
    elif user_guess > random_selection:
        print("Your guess is too high!")
        user_guess = int(input("Pick a number between 1 and 10. > "))
        i += 1

if user_guess == random_selection:
    print(f"Good guess, you win! My number was indeed {random_selection}.")
    print(f"And you were able to guess my number in only {i} tries!")





