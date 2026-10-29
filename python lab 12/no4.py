from abc import ABC, abstractmethod
import turtle

class TwoDShape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x, y, x1, y1) -> None:
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def draw(self):   
        turtle.penup()
        turtle.goto(self.x, self.y)   
        turtle.pendown()
        turtle.goto(self.x1, self.y1)

class Rectangle(TwoDShape):
    def __init__(self, x, y, w, l) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.length = l

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.length)
            turtle.right(90)

class Circle(TwoDShape):
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):       
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)


class Square(TwoDShape):
    def __init__(self, x, y, l) -> None:
        self.x = x
        self.y = y
        self.length = l

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(self.length)
            turtle.right(90)




       
        
# test code

l1 = Line(0,0,100,100)
l2 = Line(0,0,-100,100)

r1 = Rectangle(-150,-10,300,50)
r2 = Rectangle(-170,120,340,400)

c1 = Circle(-100,-100, 50)
c2 = Circle(100,-100, 50)

shape = [l1,r1,c1,l2,c2,r2]

# comment this part out if you don't want to test Square class yet

s1 = Square(-200,-100, 30)
s2 = Square(170,-100, 30)
s3 = Square(-30,-200, 60)

shape += [s1,s2,s3]

# comment to this point

for s in shape:
    s.draw()
    
turtle.done()
            