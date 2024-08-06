"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

4. Определите, содержит ли строка символ ‘a’, за которым следует 0 или 1 символ ‘b’.

* дополнительное условие:
после a может быть ТОЛЬКО 0 или 1 b, и далее не может быть b или c
то есть abc - True
        abb - False
"""
import re

contains_ab_0_or_1 = lambda s: bool(re.search(r'ab?([^bc]| )', s))

print(contains_ab_0_or_1("a "))     # True
print(contains_ab_0_or_1("abf"))    # True
print(contains_ab_0_or_1("abb"))   # True
print(contains_ab_0_or_1("abc"))   # True
print(contains_ab_0_or_1("b"))     # False

# contains_ab_0_or_1_only = lambda s: bool(re.search(r'ab?(?!b)', s))
