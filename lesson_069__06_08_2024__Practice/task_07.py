"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

7. Определите, начинается ли строка с заданного числа.
"""
import re


starts_with_number = lambda s, num: bool(re.search(..., s))

# Примеры использования
print(starts_with_number("42 is the answer", 42))  # True
print(starts_with_number("The answer is 42", 42))  # False
