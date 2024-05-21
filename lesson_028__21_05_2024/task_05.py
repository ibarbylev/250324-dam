"""Напишите функцию, которая вернет количество чётных чисел в данном массиве."""


def count_even_numbers(lst: list[int]) -> int:

    # ===== var 1 =====
    # count = 0
    # for num in lst:
    #     if num % 2 == 0:
    #         count += 1
    # return count

    # ===== var 2 =====
    # return sum(1 for ls in lst if ls % 2 == 0)

    # ===== var 3 =====
    return len([ls for ls in lst if ls % 2 == 0])


print(count_even_numbers([1, 2, 3, 4, 5]))   # 2
print(count_even_numbers([2, 4, 6, 8, 10]))  # 5
print(count_even_numbers([1, 3, 5, 7, 9]))   # 0
print(count_even_numbers([]))                # 0
print(count_even_numbers([0, 2, -2, -4]))    # 4
