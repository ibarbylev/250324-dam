"""Создать 10 объектов класса Person с разными именами,
используя список data.

Написать функцию, которая
    из списка объекта класса Person старше 18 лет
    создаёт список из объектов класса Employee,
    вычисляя возраст каждого Person по дате рождения.

Использовать map и filter.
Реализация трансформации список Person в список Employee должна быть в одну строчку.

Вывести получившихся сотрудников на экран.

Используя функцию all() убедиться, что все сотрудники действительно старше 18 лет.
"""
from typing import List

from task_04 import Person, Employee

data = [
    ("Alice", "2012-05-17"),
    ("Bob", "2005-07-23"),
    ("Charlie", "1990-08-12"),
    ("David", "1980-03-15"),
    ("Eve", "1995-02-28"),
    ("Frank", "2003-06-06"),
    ("Grace", "2001-12-30"),
    ("Heidi", "2010-11-19"),
    ("Ivan", "1999-04-01"),
    ("Judy", "1997-09-09")
]


# persons = [Person(*line) for line in data]
persons = [Person(name, birth_day) for name, birth_day in data]


def from_p_to_e(persons: List[Person]) -> List[Employee]:
    p_older_18 = filter(lambda p: p.get_age() > 18, persons)
    return [Employee(p.name, p.get_age()) for p in p_older_18]


print(*from_p_to_e(persons), sep='\n')

# Charlie, 33
# David, 44
# Eve, 29
# Frank, 21
# Grace, 22
# Ivan, 25
# Judy, 26

