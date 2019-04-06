from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="yellow")

# draw a rectangle from x0, y0 to x1, y1

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((250, 100, 250, 400), fill=color)
draw.line((250, 400, 200, 500), fill=color)
draw.line((250, 400, 300, 500), fill=color)

draw.line((250, 300, 150, 250), fill=color)
draw.line((250, 300, 350, 250), fill=color)


circle_x = width/2
circle_y = height/3.35
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='purple')

img.show()
