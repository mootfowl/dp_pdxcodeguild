'''
Lab 13: Guess the Number

Let's play 'Guess the Number'.
The computer will guess a random int between 1 and 10.
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Using a while loop, allow the user to guess 10 times.
If they fail to guess the number after 10 tries, the user is told they've lost.
If the user guesses the number, the user is told they've won and the game exits.
You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)
Below is an example run of the game:

    guess the number: 5
    try again!
    guess the number: 2
    try again!
    guess the number: 3
    correct! you guessed 3 times

'''

import random

user_guess = int(input("Let's play a game! \nI've picked a random number between 1 and 10. \nCan you guess what it is? > "))
random_selection = random.randint(1, 10)
i = 1

while random_selection != user_guess and i < 10:
    print("That was a terrible guess. Try again.")
    user_guess = int(input("Pick a number between 1 and 10. > "))
    i += 1
    if user_guess == random_selection:
        print(f"Good guess, you win! My number was indeed {random_selection}.")

else:
    print("You've lost. Better luck next time!")

