"""Дано натуральное число N.
Выведите все числа от 1 до N используя рекурсию.

* Попробуйте выполнить решение в двух вариантах: для хвостовой, и НЕ хвостовой рекурсии?
"""


def tail_recursion(n, current=1):
    if n < current:
        return
    print(current)
    tail_recursion(n, current + 1)


tail_recursion(5)


def non_tail_recursion(n):
    if n == 0:
        return n
    non_tail_recursion(n - 1)
    print(n)


non_tail_recursion(5)
