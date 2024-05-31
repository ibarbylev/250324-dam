"""Напишите программу, которая использует рекурсию для вычисления суммы цифр числа.
Создайте функцию sum_digits, которая принимает один аргумент - число,
для которого нужно вычислить сумму цифр.
Используйте условие выхода из рекурсии, когда число состоит из одной цифры.
Выведите результат на экран.

Пример вывода:
Введите число: 12345
Сумма цифр числа 12345 равна 15
"""


def sum_digits_tail_recursion(n, accumulator=0) -> int:
    if n < 10:
        return n + accumulator
    return sum_digits_tail_recursion(n // 10, n % 10 + accumulator )


def sum_digits_non_tail_recursion(n) -> int:
    if n < 10:
        return n
    return n % 10 + sum_digits_non_tail_recursion(n // 10)


for num in [123, 5555, 7684467]:
    print(sum_digits_tail_recursion(num), end=' ')
    print(sum_digits_non_tail_recursion(num), end=' ')
    print()
