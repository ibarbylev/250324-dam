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
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius


def calculate_averages(circles: List[Circle]) -> Tuple[float, float]:
    sum_area = sum(circle.get_area() for circle in circles)
    cnt = len(circles)
    avg_area = sum_area / cnt
    sum_circumference = sum(circle.get_circumference() for circle in circles)
    avg_circumference = sum_circumference / cnt
    return avg_area, avg_circumference


random.seed(42)
circles = [Circle(random.randint(10, 50)) for _ in range(10)]


av_area, av_circumference = calculate_averages(circles)
print(f"Average Area: {av_area:.2f}")
print(f"Average Circumference: {av_circumference:.2f}")

# Average Area: 2381.64
# Average Circumference: 155.19
