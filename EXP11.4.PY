import turtle


t = turtle.Turtle()
# t.penup()
# t.backward(100)  # Move left to start from a good position
# t.pendown()
# Print each line by moving the turtle down
for i in range(1,11):
    t.write(f"5 x {i} = {5*i}", font=("Arial", 14, "normal"))
    t.penup()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()

t.hideturtle()
turtle.done()
