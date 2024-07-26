"""Дополнить класс Person операцией сложения.
При сложении двух объектов этого класса
операция должна возвращать новый объект класса Person,
у которого рост - четверть от среднего арифметического роста родителей,
вес - двадцатая часть от среднего арифметического веса родителей,
год рождения - текущий.
"""
from datetime import datetime


class Person:
    def __init__(self, height: int, weight: int, birth_year: int):
        self.height = height
        self.weight = weight
        self.birth_year = birth_year

    def __add__(self, other):
        avg_height = (self.height + other.height) / 2
        avg_weight = (self.weight + other.weight) / 2
        child_height = int(avg_height / 4)
        child_weight = int(avg_weight / 20)
        child_birth_year = datetime.now().year

        return Person(child_height, child_weight, child_birth_year)

    def __str__(self):
        return (f"Person(height={self.height}, "
                f"weight={self.weight}, "
                f"birth_year={self.birth_year})")


mather = Person(168, 59, 2000)
father = Person(182, 82, 1995)

child = mather + father
print(child)  # Person(height=43, weight=3, birth_year=2024)
