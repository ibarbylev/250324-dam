"""Напишите функцию, которая принимает на вход список функций и значение,
а затем применяет композицию этих функций к значению, возвращая конечный результат.

Пример использования:

add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
functions = [add_one, double, subtract_three]
compose_functions(functions, 5) должно вывести 9

"""
from typing import Callable, TypeVar

T = TypeVar('T')


def compose_functions(funcs: list[Callable[[T], T]], value: T) -> T:
    result = value
    for func in funcs:
        result = func(result)
    return result


functions = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x - 3
]

print(compose_functions(functions, 5))