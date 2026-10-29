import turtle as t
import abc

# Add your TwoDShape classes here
from abc import ABC, abstractmethod
import turtle

class TwoDShape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, length) -> None:
        self.length = length

    def draw(self, ):
        
        turtle.forward(self.length)

class Rectangle(TwoDShape):

    def __init__(self, w, l) -> None:
        self.width = w
        self.length = l

    def draw(self):
        
        for _ in range(2):
            turtle.forward(self.length)
            turtle.right(90)
            turtle.forward(self.width)
            turtle.right(90)

class Circle(TwoDShape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def draw(self):
        
        turtle.circle(self.radius)


class Square(TwoDShape):

    def __init__(self, l) -> None:
        self.length = l

    def draw(self):
        
        
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
    
t.done()
            