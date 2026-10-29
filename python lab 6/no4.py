import turtle
t = turtle.Turtle()


def draw_polygon(x,y,side = 4, size = 100):
    t.penup()
    t.goto(x, y)
    angle = 360/side
    t.pendown()
    for i in range(side):
        t.forward(size)
        t.left(angle)


draw_polygon(10,10,5, 200)


turtle.done()