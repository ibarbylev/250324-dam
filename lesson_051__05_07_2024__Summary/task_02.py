"""Напишите функцию find_max_len(), которая 
    - принимает список строк list_strings 
    - выводит на печать самую длинную строку.
(если таких строк несколько, печатается первая справа)
    
Используйте аннотацию типов для аргументов и возвращаемого значения.
"""

from typing import List


def find_max_len(list_strings: List[str]) -> None:
    print(max(reversed(list_strings), key=len))


fruits = ['Яблоко', 'Апельсин', 'Банан', 'Виноград', 'Клубника']

find_max_len(fruits)  # Клубника
