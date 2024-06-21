"""Функция plus_two(number) возвращает результат сложения переменной number с числом 2.

Предусмотрите ситуацию, когда number не является числом.
В этом случае должна возникать ошибка и на печать выводится сообщение:
TypeError: Ожидаемый тип данных — число!


"""


def plus_two(number: int | float) -> int | float:
    if not isinstance(number, (int, float)):
        raise TypeError("Ожидаемый тип данных — число!")
    return 2 * number

try:
    plus_two("5")
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
