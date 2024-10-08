"""Написать функцию get_cars_by_color(), которая принимает
список объектов класса Car и цвет и возвращает iterator объект машин этого цвета.

Напечатать этот список, выводя название модели, год и цвет.
Использовать filter и lambda функции.
"""
from typing import Iterator, List

from task_01 import Car
from task_02 import cars


def get_cars_by_color(vehicles: List[Car], color: str) -> Iterator[Car]:
    return filter(lambda v: v.color == color, vehicles)


f_cars = get_cars_by_color(cars, 'Red')
print(*f_cars, sep='\n')

# Car(brand=Golf, year=2020, color=Red)
# Car(brand=Golf, year=2020, color=Red)
# Car(brand=Skoda, year=2022, color=Red)
# Car(brand=Sharan, year=2016, color=Red)
# Car(brand=Nissan, year=2013, color=Red)
