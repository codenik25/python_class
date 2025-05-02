import turtle

t = turtle.Turtle()

# Draw circle
t.circle(100)

# Write name
t.penup()
t.goto(0,100)
t.write("Nikunj", align="center", font=("Arial", 12, "normal"))

turtle.done()
