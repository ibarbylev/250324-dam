"""Написать функцию sum_of_even, которая принимает произвольное число параметров (целые число)
и возвращает сумму всех чётных чисел.

    sum_of_even(1, 4, 5, 10)
    # 14
"""


def sum_of_even(*args):
    return sum(num for num in args if num % 2 == 0)


print(sum_of_even(1, 4, 5, 10))  # 14
