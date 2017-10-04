'''
This is a rock-paper-scissors game with the following conditions:
    > If the computer (aka robot) wins, the game is immediately over.
    > If the player (user) wins, the robot insists playing for "best two out of three".
    > If the player wins 2 in a row, the robot escalates the stakes to best 3 out of five.
'''

# Imports the ability to randomly choose from a list of options.
import random

# Establishes some global variables, including the trio from which the robot will randomly choose, as well as the point tally.
trio = ['rock', 'paper', 'scissors']
user_points = 0
robot_points = 0

# Function that is executed when the robot loses, and includes the win-stakes escalation.
def sore_loser():
    global user_points
    while user_points < 2:
        print(f"You've won {user_points}, and I've won {robot_points}.")
        game_on()
    while user_points == 2:
        print(f"Best 3 out of 5?")
        game_on()

# Function for the core game.
def game_on():
    global user_points
    user_selection = input("One, two...THREE, go! ")
    robot_selection = "rock" #random.choice(trio)
    print(f"I chose {robot_selection} and you chose {user_selection}...")
    if user_selection == "rock" and robot_selection == "rock":
        print("It's a tie! Let's play again!")
        game_on()

    elif user_selection == "rock" and robot_selection == "paper":
        print("Paper covers rock! Suck it!")

    elif user_selection == "rock" and robot_selection == "scissors":
        print("Rock smashes scissors. Crap, you win.")
        user_points += 1
        if user_points < 2:
            print("Two out of three...?")
        else:
            print("I hate you.")
        sore_loser()

    elif user_selection == "paper" and robot_selection == "rock":
        print("Paper covers rock. Crap, you win.")
        user_points += 1
        if user_points < 2:
            print("Two out of three...?")
        else:
            print("I hate you.")
        sore_loser()

    elif user_selection == "paper" and robot_selection == "paper":
        print("It's a tie! Let's play again!")
        game_on()

    elif user_selection == "paper" and robot_selection == "scissors":
        print("Scissors cut paper! Suck it!")

    elif user_selection == "scissors" and robot_selection == "rock":
        print("Rock smashes scissors! Suck it!")

    elif user_selection == "scissors" and robot_selection == "scissors":
        print("It's a tie! Let's play again!")
        game_on()

    elif user_selection == "scissors" and robot_selection == "paper":
        print("Scissors cut paper. Dammit, you win.")
        user_points += 1
        if user_points < 2:
            print("Two out of three...?")
        else:
            print("I hate you.")
        sore_loser()

# Else statement should the player type anything other than rock, paper, or scissors.
    else:
        print("What?! Are you new? Just choose either rock, paper, or scissors, okay? Geez...")
        game_on()

# The actual start of the game.
print("Let's play a game of rock, paper, scissors.")
game_on()