"""
Создать класс Person с полями имя и дата рождения (формат str).
Создать класс Employee который содержит поле имя и возраст (int)


Создать 10 объектов класса Person с разными именами.

Написать функцию, которая
    из списка объекта класса Person старше 18 лет
    создаёт список из объектов класса Employee,
    вычисляя возраст каждого Person по дате рождения.

Использовать map и filter.
Реализация трансформации список Person в список Employee должна быть в одну строчку.

Вывести получившихся сотрудников на экран.

Используя функцию all() убедиться, что все сотрудники действительно старше 18 лет.
"""
from datetime import datetime

# Найти возраст по дате рождения
birth_day = "2000-02-18"
birthdate = datetime.strptime(birth_day, '%Y-%m-%d').date()
today = datetime.today().date()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


class Person:

    def get_age(self):
        return age


class Employee:
    pass
