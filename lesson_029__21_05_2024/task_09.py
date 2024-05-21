"""Дан список чисел. Написать функцию, которая возвращает кортеж из наибольшего элемента в списке и его индекса.
Если наибольших элементов несколько, выведите индекс первого из них.
"""


def get_max_and_index(nums: list[int]) -> tuple:
    max_num = max(nums)
    max_index = nums.index(max_num)
    return max_num, max_index


print(get_max_and_index([1, 3, 7, 7, 5]))   # (7, 2)
