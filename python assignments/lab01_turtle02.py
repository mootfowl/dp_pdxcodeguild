from turtle import *

turtle = 0
# Initial turn to point up.
left(90)
# First 90 degrees in the positive direction
while turtle < 90:
    forward(1)
    right(1)
    turtle += 1
# Second 90 degrees in the negative direction
turtle = 0
while turtle < 90:
    forward(1)
    right(1)
    turtle += 1

turtle = 0
# Third 90 degrees in the negative direction
while turtle < 90:
    forward(1)
    left(1)
    turtle += 1
# Final 90 degrees in the positive direction
turtle = 0
while turtle < 90:
    forward(1)
    left(1)
    turtle += 1
# Draws the x axis
left(90)
forward(240)
# done() is unique to turtle
done()