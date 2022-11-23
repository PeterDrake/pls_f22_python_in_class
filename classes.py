import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

r = Rectangle(3, 5)
print(r.area())

c = Circle(2)
print(c.area())

shapes = [Rectangle(3, 5), Circle(2), Circle(5), Rectangle(2, 10)]
print([s.area() for s in shapes])
