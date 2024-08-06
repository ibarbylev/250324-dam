"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

3. Определите, содержит ли строка символ ‘a’, за которым следует 1 или более символов ‘b’
"""
import re


contains_ab_1_or_more = lambda s: bool(re.search(r'ab+', s))

print(contains_ab_1_or_more("a"))     # False
print(contains_ab_1_or_more("ab"))    # True
print(contains_ab_1_or_more("abb"))   # True
print(contains_ab_1_or_more("ac"))    # False
print(contains_ab_1_or_more("b"))     # False
