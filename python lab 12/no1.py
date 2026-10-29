from math import pi

class Point:
    def __init__(self, x=0.0, y=0.0) -> None:
        self.x = x
        self.y = y

    def printInfo(self):
        print(f"Position: {self.x}, {self.y}")

class Circle(Point):
    def __init__(self, x=0, y=0, radius=0.0) -> None:
        super().__init__(x, y)
        self.radius = radius
    
    def area(self,):
        return pi * self.radius**2

    def printInfo(self):
        print(f"Position: {self.x}, {self.y}; Radius: {self.radius}; Area: {self.area():.2e}")



print("Test Point:")
p = Point(1, 2)
p.printInfo()
print("Test Circle:")
c = Circle(1, 2, 3)
c.printInfo()

# Test Output:
"""
Test Point:
Position: 1, 2
Test Circle:
Position: 1, 2; Radius: 3; Area: 28.27
"""        