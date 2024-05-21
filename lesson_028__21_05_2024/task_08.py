"""Поменяйте предыдущую задачу так, чтобы функция
 - возвращала True если в массиве стоят рядом два любых одинаковых элемента.
"""


from typing import Any


def is_double_value_in_sequence(nums: list[Any], value: Any) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] == value and nums[i + 1] == value:
            return True
    return False


print(is_double_value_in_sequence([1, 2, 2], 2))  # True
print(is_double_value_in_sequence([2, 1, 2], 2))  # False
