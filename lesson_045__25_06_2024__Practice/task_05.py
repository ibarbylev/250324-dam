"""Реализовать
    - чтение информации о клиентах из json файла
    - и превращение его в список кортежей,
      который уже будет отдаваться на вход функции validate_customers.

Формат json файла с информацией о пользователях составить самостоятельно, на своЁ усмотрение.
Например:
    [
    {“name”: “Ivan”,
    “surname”: “Petrov”,
    “birth_date”: “15-03-2017”,
    “iban”:”DE1234 0000 0000 01011 333”
     },
    {и так далее}
    ]
"""

import json
from pprint import pprint

from task_01 import users


def read_json_file(filename) -> list[tuple[str, str, str, str]]:
    new_users: list[tuple[str, str, str, str]] = []
    pass

    return new_users


pprint(read_json_file('users.json'))
