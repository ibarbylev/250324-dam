"""Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

Последний элемент списка состоит из 26 символов z.
"""
from pprint import pprint


def func() -> None:
    code_a = ord('a')  # 97
    lst = []
    for i in range(26):
        lst.append(chr(code_a + i) * (i+1))

    pprint(lst)


func()
