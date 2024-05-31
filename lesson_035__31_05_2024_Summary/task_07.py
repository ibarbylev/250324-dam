"""Универсальная функция get_area() рассчитывает площадь квадрата, прямоугольника или прямоугольного треугольника:
    def get_area(side1, side2, is_triangle=False):
        if is_triangle:
            return side1 * side2 * 0.5
        return side1 * side2, 2


Необходимо создать на её основе функции, которые вычисляют площадь только одной фигуры:
    area_square(side1)
    area_rectangle(side1, side2)
    area_right_triangle(side1, side2)

При решении необходимо использовать functools.partial
"""

from functools import partial


def get_area(side1, side2, is_triangle=False):
    if is_triangle:
        return side1 * side2 * 0.5
    return side1 * side2


area_square = partial(get_area, side2=1)
# area_rectangle = ...
# area_right_triangle = ...


print(area_square(3))  # 9
# print(area_rectangle(2, 4))  # 8
# print(area_right_triangle(2, 3))  # 3.0
