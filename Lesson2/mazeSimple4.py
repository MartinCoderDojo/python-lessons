import turtle


def move_forward():
    arrow.goto(arrow.position()[0]+25, arrow.position()[1])


def move_up():
    arrow.goto(arrow.position()[0], arrow.position()[1]+50)


def complete():
    message = turtle.Turtle()
    message.penup()
    message.hideturtle()
    message.goto(-40, 120)
    if(arrow.position()[0] == 90):
        message.write('Success', font=('Arial', 18, 'normal'))
    else:
        message.write('Try Again', font=('Arial', 18, 'normal'))


wall = turtle.Turtle()
wall.penup()
wall.goto(-125, -150)
wall.pendown()

wall.forward(100)
wall.left(90)
wall.forward(50)
wall.right(90)

for x in range(3):
    wall.forward(50)
    wall.left(90)
    wall.forward(50)
    wall.right(90)

wall.left(90)
wall.forward(50)
wall.left(90)
wall.forward(50)
wall.left(90)
wall.forward(50)

for x in range(4):
    wall.right(90)
    wall.forward(50)
    wall.left(90)
    wall.forward(50)

wall.penup()
wall.hideturtle()

arrow = turtle.Turtle()
arrow.penup()

arrow.goto(-110, -125)
arrow.left(90)

# Insert your code after this line

# End of your code

complete()
