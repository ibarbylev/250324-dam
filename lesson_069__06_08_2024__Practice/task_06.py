"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

6. Определите, содержит ли строка (вся строка, от начала до конца!)
только буквы, цифры и символ подчёркивания.
"""
import re

contains_only_alphanum_and___ = lambda s: bool(re.search(r'...', s))

# Примеры использования
print(contains_only_alphanum_and___("Hello_123"))  # True
print(contains_only_alphanum_and___("Hello 123"))  # False
