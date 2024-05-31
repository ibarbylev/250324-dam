"""Универсальная функция get_area() рассчитывает прямоугольника или прямоугольного треугольника:
    def get_area(side1, side2, is_triangle=False):
        if is_triangle:
            return side1 * side2 * 0.5
        return side1 * side2, 2


Необходимо создать на её основе функции, которые вычисляют площадь только одной фигуры:
    area_rectangle(side1, side2)
    area_right_triangle(side1, side2)

При решении необходимо использовать functools.partial
"""

from functools import partial


def get_area(side1, side2, is_triangle=False):
    if is_triangle:
        return side1 * side2 * 0.5
    return side1 * side2


area_rectangle = partial(get_area)
area_right_triangle = partial(get_area, is_triangle=True)


print(area_rectangle(2, 4))  # 8
print(area_right_triangle(2, 3))  # 3.0
