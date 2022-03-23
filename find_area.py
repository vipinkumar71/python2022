import math


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth


object1 = Rectangle(4, 6)
print(object1.area())


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi


object2 = Circle(3)
print(object2.area())
