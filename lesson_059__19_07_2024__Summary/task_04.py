"""Создайте класс Circle с конструктором,
который принимает радиус в качестве аргумента.
Включите в класс два метода:
    - get_area() для вычисления площади круга и
    - get_circumference()` для вычисления длины окружности.

Создайте экземпляр класса Circle и вызовите оба метода,
выведя результаты, округленные до 2 знаков после запятой.

Создайте список circles, состоящий из 10 экземпляров класса Circle
со СЛУЧАЙНЫМ значением радиуса в диапазоне от 10 до 50 (целые числа).

Напишите функцию, которая принимает этот список и
возвращает tuple
    - среднего значения всех площадей и
    - среднего значения длин окружностей
всех объектов списка circles.
(с точностью до двух знаков после запятой)


=====  Пример: =====
Для random.seed(42) средние значения должны составлять

Average Area: 2381.64
Average Circumference: 155.19
"""

import math
import random
from typing import List, Tuple


class Circle:
    pass


def calculate_averages(circles: List[Circle]) -> Tuple[float, float]:
    pass


random.seed(42)
circles = ...


av_area, av_circumference = calculate_averages(circles)
print(f"Average Area: {av_area:.2f}")
print(f"Average Circumference: {av_circumference:.2f}")

# Average Area: 2381.64
# Average Circumference: 155.19
