"""Напишите функцию sort_dicts_by_key(), которая принимает:
    - список словарей и
    - ключ, по которому нужно отсортировать список словарей.
Функция должна быть аннотирована с помощью аннотаций типов.
"""
from operator import itemgetter
from pprint import pprint
from typing import Any, List, Dict


def sort_dicts_by_key(dicts: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    # ==== variant 1 ====
    # return sorted(dicts, key=lambda d: d[key])

    # ==== variant 2 ====
    return sorted(dicts, key=itemgetter('age'))


example_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

# sort by key 'name'
pprint(sort_dicts_by_key(example_dicts, "name"))

# sort by key 'age'
pprint(sort_dicts_by_key(example_dicts, "age"))

