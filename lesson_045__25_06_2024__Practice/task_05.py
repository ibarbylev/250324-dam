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


def read_json_file(filename) -> list[tuple[str, str, str, str]]:
    new_users: list[tuple[str, str, str, str]] = []
    with open(filename, encoding='utf-8') as file:
        raw_list = json.load(file)
        # [{'name': '', 'surname': 'Doe', 'birth_date': '2005-03-28', 'iban': 'DE44443333222211110000'}, .... ]
        for item in raw_list:
            new_item = item.get('name'), item.get('surname'), item.get('birth_date'), item.get('iban')
            new_users.append(new_item)
    return new_users


pprint(read_json_file('users.json'))
