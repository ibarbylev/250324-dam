"""Реализуйте абстрактный базовый класс Shape (фигура),
а от него унаследуйте классы
    Rectangle (прямоугольник)
    и Circle (круг).
Класс Shape должен иметь абстрактный метод area,
который должен быть реализован в каждом дочернем классе.
Классы Rectangle и Circle также должны иметь
    метод perimeter для расчета периметра.
Выведите площадь и периметр прямоугольника и круга на экран.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(4, 7)
circle = Circle(5)

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
# Rectangle area: 28
# Rectangle perimeter: 22
