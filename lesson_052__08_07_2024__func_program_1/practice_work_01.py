"""Написать функцию more_than_value, которая проверяет, действительно ли
все элементы списка больше заданной величины.
"""


from typing import List, Union


def more_than_value(nums: List[Union[int, float]], value: Union[int, float]) -> bool:
    for i in nums:
        if i <= value:
            return False
    return True


lst = [2, 9, 4, 1, 12]
print(more_than_value(lst, 1))
print(more_than_value(lst, 0))
