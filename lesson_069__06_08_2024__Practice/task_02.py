"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

2. Определите, содержит ли строка символ ‘a’, за которым следует ноль или более символов ‘b’
"""
import re


contains_ab_0_or_more = lambda s: bool(re.search(r'...', s))

print(contains_ab_0_or_more("a"))     # True
print(contains_ab_0_or_more("ab"))    # True
print(contains_ab_0_or_more("abb"))   # True
print(contains_ab_0_or_more("ac"))    # True
print(contains_ab_0_or_more("b"))     # False

