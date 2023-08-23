import turtle

t = turtle.Turtle()

length = int(input("Length: "))
sides = int(input("Sides: "))
angle = int(input("Angle: "))
bgcolor = input("Colour: ")

t.fillcolor(bgcolor)

t.begin_fill()

for x in range(sides):
  t.forward(length)
  t.right(angle)

t.end_fill()

# more shapes ------------------------

# How to draw  a square
t.penup()
t.goto(-250,180)
t.pendown()

t.fillcolor('orange')
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.end_fill()


# How to draw a rectangle
t.penup()
t.goto(-80, 180)
t.pendown()

t.fillcolor('red')
t.begin_fill()
t.forward(300)
t.right(90)
t.forward(150)
t.right(90)
t.forward(300)
t.right(90)
t.forward(150)
t.end_fill()

# How to draw a triangle
t.penup()
t.goto(-250, -150)
t.pendown()

t.fillcolor('green')
t.begin_fill()
t.right(90)
t.forward(150)
t.right(-120)
t.forward(150)
t.right(-120)
t.forward(150)
t.end_fill()

# How to draw a parallelogram
t.penup()
t.goto(-80, -150)
t.pendown()

t.fillcolor('blue')
t.begin_fill()
t.right(-120)
t.forward(300)
t.right(-60)
t.forward(150)
t.right(-120)
t.forward(300)
t.right(-60)
t.forward(150)
t.end_fill()

# import turtle

# t = turtle.Turtle()

# length = int(input("Length: "))
# sides = int(input("Sides: "))
# angle = int(input("Angle: "))
# bgcolor = input("Colour: ")

# t.fillcolor(bgcolor)

# t.begin_fill()

# for x in range(sides):
#   t.forward(length)
#   t.right(angle)

# t.end_fill()
