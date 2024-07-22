"""Напишите декоратор validate_args, который будет
проверять типы аргументов функции и выводить сообщение об ошибке,
если переданы аргументы неправильного типа.
Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.

Пример использования:

@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")
greet(25, "Анна")  # Все аргументы имеют правильные типы
greet("25", "Анна")  # Возникнет исключение TypeError

"""


def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f'Argument {arg} is not of type {expected_type.__name__}')

            print("Все аргументы имеют правильные типы")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


try:
    greet(25, "Анна")  # Все аргументы имеют правильные типы
    greet("25", "Анна")  # Возникнет исключение TypeError
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")

