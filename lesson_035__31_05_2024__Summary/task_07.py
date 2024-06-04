"""Универсальная функция get_area() рассчитывает площадь прямоугольника или прямоугольного треугольника:
    def get_area(side1, side2, is_triangle=False):
        if is_triangle:
            return side1 * side2 * 0.5
        return side1 * side2, 2


Необходимо создать на её основе функции, которые вычисляют площадь только одной фигуры:
    rectangle_area(side1, side2)
    right_triangle_area(side1, side2)

При решении необходимо использовать functools.partial
"""

from functools import partial


def get_area(side1, side2, is_triangle=False):
    if is_triangle:
        return side1 * side2 * 0.5
    return side1 * side2


rectangle_area = partial(get_area)
right_triangle_area = partial(get_area, is_triangle=True)


print(rectangle_area(2, 4))  # 8
print(right_triangle_area(2, 3))  # 3.0
