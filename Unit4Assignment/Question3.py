import turtle

t = turtle.Turtle()

t.goto(0, 0)

data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in data:
    t.left(angle)
    t.forward(100)

print(t.heading())

