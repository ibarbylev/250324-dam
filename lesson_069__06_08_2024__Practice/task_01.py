"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

1. Определите, содержит ли заданная строка набор данных символов (a-z, A-Z и 0-9).
"""
import re

contains_alphanumeric = lambda s: bool(re.search(r'...', s))

print(contains_alphanumeric("Hello123"))  # True
print(contains_alphanumeric("!@#$%^"))    # False

