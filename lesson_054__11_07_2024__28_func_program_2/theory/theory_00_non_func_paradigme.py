"""Пример НЕ функционального программирования"""


def fn():
    for idx, n in enumerate(nums):
        nums[idx] = n ** 2


nums = [1, 2, 3]
fn()
print(nums)  # [1, 4, 9]
