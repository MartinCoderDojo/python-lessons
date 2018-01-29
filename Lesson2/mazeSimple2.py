import turtle


def moveforward():
    arrow.goto(arrow.position()[0]+55, arrow.position()[1])


def moveup():
    arrow.goto(arrow.position()[0], arrow.position()[1]+55)


def complete():
    message = turtle.Turtle()
    message.penup()
    message.hideturtle()
    message.goto(-40, 100)
    if(arrow.position()[0] == 140):
        message.write('Success', font=('Arial', 18, 'normal'))
    else:
        message.write('Try Again', font=('Arial', 18, 'normal'))


wall = turtle.Turtle()
wall.penup()
wall.goto(-150, -150)
wall.pendown()
for x in range(2):
    wall.forward(100)
    wall.left(90)
    wall.forward(50)
    wall.right(90)

wall.forward(100)
wall.left(90)
wall.forward(50)
wall.left(90)

wall.forward(150)
wall.left(90)
wall.forward(50)
wall.right(90)

wall.forward(100)
wall.left(90)
wall.forward(50)
wall.right(90)
wall.forward(50)
wall.left(90)
wall.forward(50)
wall.penup()
wall.hideturtle()

arrow = turtle.Turtle()
arrow.penup()
arrow.goto(-135, -125)
arrow.left(90)

# Insert your code after this line

# End of your code

complete()
