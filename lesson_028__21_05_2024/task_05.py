"""Напишите функцию, которая вернет количество чётных чисел в данном массиве."""


def count_even_numbers(lst: list[int]) -> int:
    return ...


print(count_even_numbers([1, 2, 3, 4, 5]))   # 2
print(count_even_numbers([2, 4, 6, 8, 10]))  # 5
print(count_even_numbers([1, 3, 5, 7, 9]))   # 0
print(count_even_numbers([]))                # 0
print(count_even_numbers([0, 2, -2, -4]))    # 4
