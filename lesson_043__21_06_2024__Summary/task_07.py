"""Дополните условия предыдущей задачи более точным определением ошибочно введённого типа данных number:
Для строки: TypeError: Ошибка! Строка вместо числа!
Для списка: TypeError: Ошибка! Список вместо числа!
Для множества: TypeError: Ошибка! Множество вместо числа!


"""


def plus_two(number: int | float) -> int | float:
    pass


try:
    plus_two("1")
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")

try:
    plus_two([1, 2, 3])
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")

try:
    plus_two({1, 2, 5})
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")