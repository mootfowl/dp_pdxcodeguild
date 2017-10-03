from turtle import *

symmetry = 50

# head
left(90)
forward(symmetry)
right(90)
forward(symmetry)
right(90)
forward(symmetry)
right(90)
forward(symmetry)

# shoulders and arms
right(180)
forward(symmetry / 2)
right(90)
forward(25)
right(90)
forward(2 * symmetry)
right(180)
forward(4 * symmetry)
left(180)
forward(2 * symmetry)
left(90)
forward(symmetry)
right(45)
forward(2 * symmetry)
right(180)
forward(2 * symmetry)
right(90)
forward(2 * symmetry)


done()