"""Напишите функцию get_min, которая принимает произвольное количество аргументов
и находит минимальное число среди них.

Пример ввода: get_min(3, 10, 22, -3, 0)

Пример вывода: -3
"""


def get_min(*args: int) -> int:
    return min(args)


print(get_min(3, 10, 22, -3, 0))
