import turtle
import random
reduction_ratio = 0.618
class Draw:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def resize(self):
        self.size *= reduction_ratio

    def repositioning(self):
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
#num_sides = random.randint(3, 5) # triangle, square, or pentagon
#size = random.randint(50, 150)
#orientation = random.randint(0, 90)
#location = [random.randint(-300, 300), random.randint(-200, 200)]
#color = get_new_color()
#border_size = random.randint(1, 10)
#draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
#reduction_ratio = 0.618

# reposition the turtle and get a new location
#turtle.penup()
#turtle.forward(size*(1-reduction_ratio)/2)
#turtle.left(90)
#turtle.forward(size*(1-reduction_ratio)/2)
#turtle.right(90)
#location[0] = turtle.pos()[0]
#location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
#size *= reduction_ratio

# draw the second polygon embedded inside the original
art_style = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = Draw.get_new_color()
border_size = random.randint(1, 10)
if art_style == 1:
    pass
if art_style == 5:
    for i in range(30):
        pic = Draw(3,size, orientation, location, color, border_size)
        Draw.draw_polygon(pic)
        reduction_ratio = 0.618
        pic.color = Draw.get_new_color()
        Draw.repositioning(pic)
        Draw.resize(pic)
        Draw.draw_polygon(pic)
        Draw.resize(pic)
        Draw.draw_polygon(pic)




# hold the window; close it by clicking the window close 'x' mark
turtle.done()