"""Из класса Shape наследуем класс Square (квадрат)
и класс RightTriangle (прямоугольный треугольник),
используя функцию super()
"""


class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self):
        attrs = ', '.join(f'{k}={v}' for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class Square(Shape):
    pass


class RightTriangle(Shape):
    pass


sq = Square(4)
print(sq)
print(sq.get_area())

rt = RightTriangle(4, 4)
print(rt)
print(rt.get_area())

# Square(side=4)
# 16
# RightTriangle(side1=4, side2=4)
# 8
