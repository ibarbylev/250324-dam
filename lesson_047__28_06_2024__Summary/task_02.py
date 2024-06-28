"""Создайте функцию get_sequence(lst, tries), которая
будет проходиться по элементам списка lst (целые числа)
заданное количество раз (tries) циклически.
Один раз - один элемент списка.
После вывода последнего значения последовательности процедура начнется с самого начала.

Например, если в списке 2 элемента, а функция получила значение 3,
то сначала выведется первый объект, потом последний, а потом опять первый.
Результат работы функции представьте в виде строки, состоящей из tries количества символов
"""
from typing import Iterator


def infinitely_repeating_list(lst) -> Iterator:
    while True:
        yield from lst


def get_sequence(lst: list, tries: int) -> str:
    result = ''
    g = infinitely_repeating_list(lst)
    for i in range(tries):
        x = g.__next__()
        result += str(x)

    return result


print(get_sequence([1, 2, 3], 10))   # 1231231231
print(get_sequence([1, 2, 3, 4, 5], 8))  # 12345123
