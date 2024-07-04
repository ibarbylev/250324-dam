"""Напишите функцию count_products, которая
    - принимает список пар (клиент, продукт)
    - и возвращает словарь, где каждому имени соответствует словарь, где
        - где ключ - продукт,
        - а значение -  количество раз, которое этот продукт встречается у клиента.

Используйте аннотацию типов для аргументов и возвращаемого значения.
"""
from pprint import pprint
from typing import List, Tuple, Dict

pairs = [
    ("Alice", "Apple"),
    ("Bob", "Banana"),
    ("Alice", "Apple"),
    ("Alice", "Banana"),
    ("Bob", "Apple"),
    ("Alice", "Banana"),
    ("John", "Apple"),
]


def count_products(pairs):
    pass


result = count_products(pairs)
pprint(result)

# {'Alice': {'Apple': 2, 'Banana': 2},
#  'Bob': {'Apple': 1, 'Banana': 1},
#  'John': {'Apple': 1}}
