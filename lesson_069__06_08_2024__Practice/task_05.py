"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

5. Определите, содержит ли строка символ z.
"""
import re

contains_z = lambda s: bool(re.search(r'...', s))

print(contains_z("zebra"))    # True
print(contains_z("pizza"))    # True
print(contains_z("house"))    # False
print(contains_z("Zoo"))      # False


