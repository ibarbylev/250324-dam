"""Создайте класс Rectangle для представления прямоугольника.
Класс должен иметь атрибуты
    - width (ширина)
    - и height (высота) со значениями по умолчанию,
а также методы
    - calculate_area() для вычисления площади прямоугольника
    - и calculate_perimeter() для вычисления периметра прямоугольника.
Переопределить методы __str__, __repr__.
Затем создайте экземпляр класса Rectangle и выведите
    - информацию о нём,
    - его площадь
    - и периметр.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def calculate_perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'


rect = Rectangle(4, 5)
print(rect)
print(repr(rect))
print(f"Area: {rect.calculate_area()}")
print(f"Perimeter: {rect.calculate_perimeter()}")
