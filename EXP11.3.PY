import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, 100)
t.pendown()

for i in range(1, 6):
    t.write("* " * i, font=("Arial", 14, "normal"))
    t.penup()
    t.goto(-100, 100 - i * 30)
    t.pendown()

t.hideturtle()
turtle.done()
