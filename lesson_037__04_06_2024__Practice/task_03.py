"""Дано натуральное число N.
Написать функцию digits_sum(N), которая вычисляет сумму его цифр.
При решении этой задачи пользуемся рекурсией, а строки, списки, массивы и циклы не используем.
Пример digits_sum(179) = 17
"""


def digits_sum_non_tail(n):
    if n < 10:
        return n
    else:
        return n % 10 + digits_sum_non_tail(n // 10)


print(digits_sum_non_tail(179))  # 17


def digits_sum_tail(n, accumulator=0):
    if n < 1:
        return accumulator
    return digits_sum_tail(n // 10, n % 10 + accumulator)


print(digits_sum_tail(179))  # 17

