class Square:
    def __init__(self, value, value2=0):
        self.side = value
        self.side2 = value2

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


square = Square(3, 5)
# square.side2 = 20
print(square.side2)
s2 = Square(5)
print(square.side)
print(square.area())
print(square.perimeter())


class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return (self.side1 + self.side2) * 2


rect = Rectangle(3, 4)
rect2 = Rectangle(5, 10)
print(rect.area())
print(rect2.area())
