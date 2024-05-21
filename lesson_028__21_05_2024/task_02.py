"""Дано два массива целых чисел. Написать функцию, которая
 - возвращает true, если их первые или последние элементы равны.
Оба массива минимальной длины 1.
"""


def first_item_equal_last(lst_1: list[int], lst_2: list[int]) -> bool:
    return ...


print(first_item_equal_last([6], [6]))                      # True
print(first_item_equal_last([6, 1, 3], [6, 2, 3, 4, 3]))    # True
print(first_item_equal_last([5, 6], [6, 5, 5, 5]))          # False
print(first_item_equal_last([5], [5, 1, 5]))                # True
