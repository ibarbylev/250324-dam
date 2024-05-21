"""Дан массив целых чисел.
Написать функцию, которая
 - вернет True, если 6 является первым или последним элементом массива,
 - и False в противном случае.
 Массив минимальной длины 1.
"""


def is_6_start_or_end(lst: list[int]) -> bool:
    return lst[0] == 6 and lst[-1] == 6


print(is_6_start_or_end([6]))        # True
print(is_6_start_or_end([6, 1, 6]))  # True
print(is_6_start_or_end([5, 6]))     # False
print(is_6_start_or_end([5]))        # False
