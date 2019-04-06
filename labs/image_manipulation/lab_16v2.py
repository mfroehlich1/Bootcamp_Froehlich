from PIL import Image
import colorsys

img = Image.open("Lenna_(test_image).png") # must be in same folder
width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y,]

        brightness = int(0.299*r + 0.587*g + 0.114*b)

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        v += v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[x, y] = (b, r, g)

img.show().load()
