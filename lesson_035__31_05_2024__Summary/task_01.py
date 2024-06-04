"""Необходимо написать функцию raising_to_power(), которая принимает список чисел nums и степень power.
Функция возвращает список этих чисел, возведённых в указанную степень.

Важно: и список nums, и значение переменной power,  после выполнения функции должны остаться неизменными.

nums = [1, 2, 3]
value = 2
print(raising_to_power(nums, value))  # [1, 4, 9]

print(nums)   # [1, 2, 3]
print(value)  # 2

"""


def raising_to_power(nums: list[int], power: int) -> list[int]:
    return [num ** power for num in nums]


nums = [1, 2, 3]
value = 2
print(raising_to_power(nums, value))  # [1, 4, 9]

print(nums)   # [1, 2, 3]
print(value)  # 2
