'''
LAB18 v2: Image Manipulation


Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue.
If you don't have colorsys installed, run pip install colorsys in a terminal.
Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255.
You'll have to convert between these two representations.

'''

from PIL import Image
import colorsys

img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # print(r, g, b)
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        # print(h, s, v)
        h, s, v = h, s * 2, v
        # print(h, s, v)
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        # print(r, g, b)
        pixels[i, j] = (r, g, b)

img.show()