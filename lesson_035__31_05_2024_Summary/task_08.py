"""Дано натуральное число N. Вычислите сумму его цифр.

При решении этой задачи нельзя использовать строки, списки, массивы, циклы.

Задачу необходимо решить с помощью рекурсии.
"""


# ============== tail recursion =================
def sum_digits_tail(num, accumulator=0):
    if num < 1:
        return accumulator
    else:
        return sum_digits_tail(num // 10, num % 10 + accumulator)


print(sum_digits_tail(246))  # 12


# ============== non tail recursion =================
def sum_digits_non_tail(num):
    if num < 10:
        return 0
    else:
        return num % 10 + sum_digits_tail(num // 10)


print(sum_digits_non_tail(246))  # 12
