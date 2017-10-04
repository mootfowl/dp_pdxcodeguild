'''
This program converts a numeric grade of values between 0 and 100 into a letter grade.
As a little extra bit of fun, if the user enters an A grade between 90-100, the program draws a star for them using
the turtle drawing module.
'''


# This line imports the turtle module.
from turtle import *

# This function draws the star and is called when a value equivalent to an A is entered.
def star():
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)

    done()

# Prompts the user to enter a number, and then converts the input string into an integer which can later be compared to other integers.
# If the user enters something that cannot be converted to an integer, they are prompted again.

while True: # Infinite loop
    try:
        numeric_grade = int(input("Enter a number between 0 and 100 > ")) # Creates an integer from the input value.
        break
    except ValueError:
        print("Whoops, that was not a valid number. Try again.")

# These conditionals determine the letter grade based on the input value.
if numeric_grade < 60:
    print("You've earned an F. Maybe basket weaving is more your speed...?")

elif numeric_grade < 70:
    print("Your grade is a D. As in, 'Don't quit your dayjob'.")

elif numeric_grade < 80:
    print("'C is for cookie, that's good enough for me.' \n- Cookie Monster")

elif numeric_grade < 90:
    print("Your grade is a B. Just a little BETTER than average.")

elif numeric_grade >= 90 and numeric_grade <= 100:
    print("Well done on your A grade! You get a star!")
    star()

else:
    print("You're not very good at following instructions, are you?")

