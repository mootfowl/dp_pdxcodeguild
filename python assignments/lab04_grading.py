from turtle import *

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

numeric_grade = input("Enter a number between 0 and 100 > ")
numeric_grade = int(numeric_grade)

if numeric_grade < 60:
    print("You've earned an F. Maybe basket weaving is more your speed...?")

elif numeric_grade < 70:
    print("Your grade is a D. As in, 'Don't quit your dayjob'.")

elif numeric_grade < 80:
    print("'C is for cookie, that's good enough for me.' \n- Cookie Monster")

elif numeric_grade < 90:
    print("Your grade is a B.")

else:
    print("Well done on your A grade! You get a star!")
    star()

