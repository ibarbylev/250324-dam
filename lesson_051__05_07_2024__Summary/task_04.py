"""Имеется 2 списка целых чисел одинаковой длины.
Необходимо написать функцию get_new_list(action, lst1, lst2),
которая принимает
 - объект operation (add, sub, mul, truediv)
 - список lst1
 - список lst2
И возвращает новый список, содержащий сумму, разность, произведение или деление
соответствующих элементов двух списков.

Важно: известно, что список lst2 не содержит нулевых значений.
Используйте аннотацию типов для аргументов и возвращаемого значения.
"""
from typing import Callable, List
from operator import add, sub, mul, truediv

lst1 = [2, 3, 4]
lst2 = [2, 3, 4]


def get_new_list(action: Callable, lst1: List[int], lst2: List[int]) -> List[int | float]:
    return list(map(action, lst1, lst2))


print(get_new_list(add, lst1, lst2))
print(get_new_list(sub, lst1, lst2))
print(get_new_list(mul, lst1, lst2))
print(get_new_list(truediv, lst1, lst2))

# [4, 6, 8]
# [0, 0, 0]
# [4, 9, 16]
# [1.0, 1.0, 1.0]
