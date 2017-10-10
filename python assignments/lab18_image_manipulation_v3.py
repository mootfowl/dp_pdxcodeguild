# from PIL import Image, ImageDraw
# from random import randint
#
# width = 500
# height = 500
#
# img = Image.new('RGB', (width, height))
# draw = ImageDraw.Draw(img)
#
# for i in range(1000):
#     x0 = randint(0, width)
#     y0 = randint(0, height)
#     x1 = randint(0, width)
#     y1 = randint(0, height)
#     line_width = randint(1, 40)
#     red = randint(0, 255)
#     green = randint(0, 255)
#     blue = randint(0, 255)
#     draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)
#
# img.show()

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

# Draw two arms
draw.line((20, 20, width / 2, height / 3), fill="lightblue")
draw.line((480, 20, width / 2, height / 3), fill="lightblue")

# Draw center torso
draw.line((250, 100, 250, 300), fill="lightblue")

# Draw legs
draw.line((250, 300, 20, 480), fill="lightblue")
draw.line((250, 300, 480, 480), fill="lightblue")



# draw.line((0, height, width, 0), fill="lightblue")


circle_x = width/2
circle_y = height/6
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightblue')

img.show()