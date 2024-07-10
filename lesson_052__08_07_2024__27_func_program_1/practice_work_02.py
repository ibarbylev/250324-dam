"""Измените решение предыдущей задачи,
применяя парадигму функционального программирования.
"""


def more_than_value(nums: list[int | float], value: int | float) -> bool:
    return all(n > value for n in nums)


lst = [2, 9, 4, 1, 12]
print(more_than_value(lst, 1))
print(more_than_value(lst, 0))
