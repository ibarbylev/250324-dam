"""Напишите функцию get_largest_string(), которая
 - принимает список строк
 - и возвращает наибольшую строку из списка.
Функция должна быть аннотирована с помощью аннотаций типов.
"""
from typing import List


def get_largest_string(strings: List[str]) -> str:
    if not strings:
        return ""
    return max(strings, key=len)


lst = ["apple", "banana", "pear", "grape", "orange"]
print(get_largest_string(lst))  # banana

