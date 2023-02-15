import turtle

num_sides = int(input("Enter the number of sides for your polygon: "))
side_length = int(input("Enter the length of the sides of your polygon: "))
color = input("Enter the color of your polygon: ")
fill_color = input("Enter the fill color of your polygon: ")

t = turtle.Turtle()

t.fillcolor(fill_color)

t.penup()
t.pendown()

t.color(color)
t.begin_fill()
for i in range(num_sides):
    t.forward(side_length)
    t.left(360/num_sides)
t.end_fill()

turtle.done()
