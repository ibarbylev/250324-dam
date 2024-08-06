"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

9. Определите, содержит ли строка цифры в конце.
"""
import re


ends_with_digits = lambda s: bool(re.search(r'...', s))

# Примеры использования
print(ends_with_digits("This is a test 123"))  # True
print(ends_with_digits("This is a test"))      # False
