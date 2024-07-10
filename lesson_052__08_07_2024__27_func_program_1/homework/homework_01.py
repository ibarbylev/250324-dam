"""Напишите функцию , которая принимает на вход список чисел и
возвращает сумму квадратов только чётных чисел из списка,
используя функциональные подходы (например, map, filter и reduce).

Пример вывода:
Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
Результат: 72
"""

from functools import reduce


def sum_of_squares_of_even_nums(nums):
    even_nums = filter(lambda x: x % 2 == 0, nums)
    sq_even_nums = map(lambda x: x ** 2, even_nums)
    result = reduce(lambda x, y: x + y, sq_even_nums)
    return result


nums = [4, 6, 3, 4, 2, 3, 9, 0, 7]
print("Результат:", sum_of_squares_of_even_nums(nums))
