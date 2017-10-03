from turtle import *

turtle = 0
unit = 15
# Initial turn to point up.
left(90)
# First 90 degrees in the positive direction
while turtle < 90:
    forward(unit)
    right(unit)
    turtle += unit
# Second 90 degrees in the negative direction
turtle = 0
while turtle < 90:
    forward(unit)
    right(unit)
    turtle += unit

turtle = 0
# Third 90 degrees in the negative direction
while turtle < 90:
    forward(unit)
    left(unit)
    turtle += unit
# Final 90 degrees in the positive direction
turtle = 0
while turtle < 90:
    forward(unit)
    left(unit)
    turtle += unit

# done() is unique to turtle
done()