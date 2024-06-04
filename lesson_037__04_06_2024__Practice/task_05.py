"""Дано целое число, заканчивающаяся цифрой 0.
Выведите последовательность цифр этого числа в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных,
а нужно пользоваться рекурсией.
"""


def recurse_reverse(num, accumulator=0):
    if num < 1:
        return accumulator
    return recurse_reverse(num // 10, num % 10 + accumulator * 10)


print(recurse_reverse(1520))   # 251
