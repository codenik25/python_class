import turtle

t = turtle.Turtle()
t.speed(2)

# Draw face (circle)
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw left eye
t.penup()
t.goto(-35, 35)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw right eye
t.penup()
t.goto(35, 35)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.circle(50, 120)

t.hideturtle()
turtle.done()
