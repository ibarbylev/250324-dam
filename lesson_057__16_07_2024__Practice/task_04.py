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


class Person:
    def __init__(self, name: str, birth_day: str):
        self.name = name
        self.birth_day = birth_day

    def __str__(self):
        return f'{self.name}, {self.birth_day}'

    def get_age(self):
        birthdate = datetime.strptime(self.birth_day, '%Y-%m-%d').date()
        today = datetime.today().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'


if __name__ == '__main__':
    p = Person('Alex', '1987-09-12')
    print(p.get_age())