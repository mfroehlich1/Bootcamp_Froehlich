from PIL import Image

img = Image.open("Lenna_(test_image).png") # must be in same folder
width, height = img.size
pixels = img.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y,]

        brightness = int(0.299*r + 0.587*g + 0.114*b)

        pixels[x, y] = (b, r, g)

img.show()
