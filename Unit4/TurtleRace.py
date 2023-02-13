import turtle              # 1.  import the modules
import random


window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

turtle1 = turtle.Turtle()    # 3.  Create two turtles
turtle2 = turtle.Turtle()
turtle1.color('red')
turtle2.color('blue')
turtle1.shape('turtle')
turtle2.shape('turtle')

turtle2.up()                  # 4.  Move the turtles to their starting point
turtle1.up()
turtle2.goto(-400, 20)
turtle1.goto(-400,-20)

while True:
    turtle1xdir = random.randrange(0, 10)
    turtle2xdir = random.randrange(0, 10)
    turtle1.forward(turtle1xdir)
    turtle2.forward(turtle2xdir)
    if turtle1.xcor() > 400 or turtle2.xcor() > 400:
        break

# your code goes here

window.exitonclick()
