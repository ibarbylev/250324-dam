"""Напишите функцию, которая принимает список словарей и ключ, по которому нужно отсортировать список словарей.
Функция должна быть аннотирована с помощью аннотаций типов.
"""
from operator import itemgetter

data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]


def sort_dict(lst_dict, key_value):
    return sorted(lst_dict, key=itemgetter(key_value))


print(sort_dict(data, "age"))
