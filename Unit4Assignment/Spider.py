import turtle
screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("lightgreen")
t.color("blue")
t.shape("turtle")

for i in range(12):
    t.goto(0,0)
    t.up()
    t.forward(120)
    t.down()
    t.forward(20)
    t.up()
    t.forward(20)
    t.stamp()
    t.right(30)
t.goto(0,0)