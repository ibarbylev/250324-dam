"""Напишите программу, которая создает именованный кортеж Person
для хранения информации о человеке, включающий поля name, age и city.
Создайте список объектов Person и выведите информацию о каждом человеке на экран.

Пример вывода:

Name: Alice, Age: 25, City: New York
Name: Bob, Age: 30, City: London
Name: Carol, Age: 35, City: Paris
"""

from collections import namedtuple


Person = namedtuple("Person", ["name", "age", "city"])

persons = [
    Person('Alice', 25, 'New York'),
    Person('Bob', 30, 'London'),
    Person('Carol', 35, 'Paris'),
]

for person in persons:
    name, age, city = person
    print(f"Name: {name}, Age: {age}, City: {city}")

