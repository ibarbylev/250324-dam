"""Создать класс Shape, описывающий абстрактную фигуру,
у которой есть площадь. У этого класса есть метод calculate_area(),
который возвращает площадь фигуры.
У класса также есть атрибут экземпляра класса name,
которое содержит строчное название фигуры.
Например, “круг”, “прямоугольник” и так далее.

Метод __str__() должен содержать имя класса,
а также перечень всех атрибутов:
ClassName(attr1=value1, attr2=value2, ...)

Унаследовать от класса Shape 3 других класса:
Circle, Square, Rectangle.
У каждого класса должны быть соответствующие атрибуты,
необходимые для вычисления площади фигуры.

Для каждого класса переопределить метод calculate_area(),
который вычисляет площадь фигуры.
"""
from math import pi as PI


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

    def __str__(self):
        """ClassName(attr1=value1, attr2=value2, ...)"""
        attrs_string = [f"{k}={v}" for k, v in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(attrs_string)})"


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return round(PI * self.radius ** 2, 2)


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, name, side1, side2):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return self.side1 * self.side2


if __name__ == '__main__':
    r = Rectangle("rectangle", 3, 4)
    c = Circle("circle", 3)
    sq = Square("square", 4)

    print(r)
    print(c)
    print(sq)

    print(r.calculate_area())
    print(c.calculate_area())
    print(sq.calculate_area())

    # Rectangle(name=rectangle, side1=3, side2=4)
    # Circle(name=circle, radius=3)
    # Square(name=square, side=4)
    # 12
    # 28.274333882308138
    # 16
