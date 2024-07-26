"""Напишите декоратор, который делает так,
что задекорированная функция принимает все свои порядковые аргументы
 в порядке, обратном тому, в котором их передали.
(для именованных аргументов (kwargs) порядок не важен,
поэтому мы их здесь не учитываем).
"""


def reverse_args_decorator(func):
    def wrapper(*args):
        new_args = args[::-1]
        func(*new_args)
    return wrapper


@reverse_args_decorator
def print_args(a, b, c):
    print(f'a: {a}, b: {b}, c: {c}')


print_args(1, 2, 3)
# a: 3, b: 2, c: 1
