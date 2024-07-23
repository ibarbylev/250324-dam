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
        pass


class Circle(Shape):
    pass


class Square(Shape):
    pass


class Rectangle(Shape):
    pass


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
