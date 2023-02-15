import turtle

# Set up the turtle
t = turtle.Turtle()

# Draw an equilateral triangle
for i in range(3):
    t.forward(100)
    t.left(120)

# Move to the next position
t.penup()
t.forward(-150)
t.pendown()

# Draw a square
for i in range(4):
    t.forward(100)
    t.left(90)

# Move to the next position
t.penup()
t.left(-90)
t.forward(50)
t.pendown()

# Draw a hexagon
for i in range(6):
    t.forward(20)
    t.left(60)

# Move to the next position
t.penup()
t.left(90)
t.forward(200)
t.pendown()

# Draw an octagon
for i in range(8):
    t.forward(20)
    t.left(45)

# Exit the turtle program
turtle.done()