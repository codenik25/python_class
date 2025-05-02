import turtle

t = turtle.Turtle()

side = 40  # Starting side length
increase = 20  # Increase in side length each time

for i in range(5):
    for _ in range(4):
        t.forward(side)
        t.left(90)
    t.penup()
    t.backward(increase / 2)
    t.right(90)
    t.forward(increase / 2)
    t.left(90)
    t.pendown()
    side += increase

turtle.done()
