import turtle
t = turtle.Turtle()
t.speed(0)

def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def draw(x):
    
    #hori and verti
    size = 50

    biggest = size * x
    t.penup()
    t.goto(-biggest / 2, 0)
    t.pendown()
    t.forward(biggest)

    t.penup()
    t.left(90)
    t.goto( 0, -biggest / 2)
    t.pendown()
    t.forward(biggest)

    t.setheading(0)

    for i in range(1, x+1):
        t.penup()
        square_size = i * size
        print(square_size)
        t.goto(-square_size / 2, -square_size / 2)
        t.pendown()
        square(square_size)

draw(4)
turtle.done()