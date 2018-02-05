import turtle


def move_forward():
    arrow.goto(arrow.position()[0]+90, arrow.position()[1])


def complete():
    message = turtle.Turtle()
    message.penup()
    message.hideturtle()
    message.goto(-40, 100)
    if(arrow.position()[0] == 135):
        message.write('Success', font=('Arial', 18, 'normal'))
    else:
        message.write('Try Again', font=('Arial', 18, 'normal'))


wall = turtle.Turtle()
wall.penup()
wall.goto(-150, 0)
wall.pendown()
wall.forward(300)
wall.right(90)
wall.forward(50)
wall.right(90)
wall.forward(300)
wall.right(90)
wall.forward(50)
wall.penup()
wall.hideturtle()

arrow = turtle.Turtle()
arrow.penup()
arrow.goto(-135, -25)
arrow.left(90)

# Insert your code after this line

# End of your code

complete()
