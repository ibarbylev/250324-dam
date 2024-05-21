"""Напишите функцию, которая принимает список кортежей от пользователя,
где каждый кортеж содержит информацию о студенте (имя, возраст, средний балл).
Программа должна вывести на экран имена студентов, чей средний балл выше заданного значения.
Используйте методы кортежей и циклы для обработки данных.
Выведите итоговый список на экран с помощью команды print.

Пример списка кортежей:

[("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
Пример вывода:
Студенты со средним баллом выше 90 : ['Charlie']
"""


def list_of_honors(persons: list[tuple], value: int) -> None:
    honor_students = []
    for person in persons:
        name, age, gpa = person   # gpa - grade point average
        if gpa >= value:
            honor_students.append(name)
    print(f'Студенты со средним баллом выше {value} : {honor_students}')


lst = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
list_of_honors(lst, 90)
list_of_honors(lst, 91)
