"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

1. Определите, содержит ли заданная строка набор данных символов (a-z, A-Z и 0-9).
"""
import re


def contains_alphanumeric(text):
    return bool(re.search(r'[0-9a-zA-Z]+', text))


print(contains_alphanumeric("Hello123"))  # True
print(contains_alphanumeric("!@#$%^"))    # False

