"""Написать программу, вычисляющую факториал числа.
Решить задачу с помощью рекурсии.
"""


def factorial_loop(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact


def factorial_tail_recursion(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail_recursion(n-1, n * accumulator)


def factorial_non_tail_recursion(n):
    if n <= 1:
        return 1
    return n * factorial_non_tail_recursion(n-1)


for i in range(5):
    print(factorial_loop(i), end=' ')
    print(factorial_tail_recursion(i), end=' ')
    print(factorial_non_tail_recursion(i), end=' ')
    print()
