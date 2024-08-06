"""Написать программу, которая использует функции языка для работы
с регулярными выражениями и синтаксис регулярных выражений:

10. Найдите вхождения и позиции подстроки в строке.
    Пример: строка “Домашние задания, задания в классе, отпускные задания”,
    подстрока “задания”,
    вывод “задания” на 9:15, “задания” на 18:24, “задания” на 46:52.
"""
import re
from typing import List


def find_substring_positions(text: str, substring: str) -> List[str]:
    matches = re.finditer(substring, text)
    # matches [<re.Match object; span=(9, 16), match='задания'>,
    #          <re.Match object; span=(18, 25), match='задания'>,
    #          <re.Match object; span=(46, 53), match='задания'>]

    #           match in matches:
    #                   match.start()  # 9
    #                   match.end()    # 16
    #                   ..................






text = "Домашние задания, задания в классе, отпускные задания"
substring = "задания"
positions = find_substring_positions(text, substring)
for position in positions:
    print(position)

# "задания" на 9:16
# "задания" на 18:25
# "задания" на 46:53
