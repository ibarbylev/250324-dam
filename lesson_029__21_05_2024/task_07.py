"""Написать функцию, которая возвращает True, если в массиве две двойки идут подряд.
[1, 2, 2] -> True,
[2, 1, 2] -> False
"""


def is_double_2_in_sequence(nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


print(is_double_2_in_sequence([1, 2, 2]))  # True
print(is_double_2_in_sequence([2, 1, 2]))  # False
