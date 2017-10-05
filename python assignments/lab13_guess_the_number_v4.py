'''
Lab 13: Guess the Number
Version 4

Tell the user whether their current guess is closer than their last.
This can be done by maintaining a variable containing the last guess outside the loop,
then comparing the last guess to the current guess, and check if it's closer.
Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).
'''

# Note: This program works...ish. But I still need to find tune it.

import random

random_selection = random.randint(1, 10)
all_guesses = []
user_guess = 0

print("I've picked a random number between 1 and 10. \nCan you guess what it is?")

while random_selection != user_guess:
    user_guess = int(input("Pick a number between 1 and 10. > "))
    # print(all_guesses)
    if len(all_guesses) != 0:
        if abs(all_guesses[-1] - random_selection) < abs(user_guess - random_selection):
            print("Your last guess was closer to my random number.")

        elif abs(all_guesses[-1] - random_selection) > abs(user_guess - random_selection):
            print("Your last guess was farther from my random number.")
    print("Not quite...")
    all_guesses.append(user_guess)

if user_guess == random_selection:
    print(f"Good guess, you win! My number was indeed {random_selection}.")





