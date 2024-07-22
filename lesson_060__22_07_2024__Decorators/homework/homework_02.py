"""Напишите декоратор log_args, который будет записывать аргументы
и результаты вызовов функции в лог-файл.
Каждый вызов функции должен быть записан на новой строке в формате
"Аргументы: <аргументы>, Результат: <результат>".

Используйте модуль logging для записи в лог-файл.

Пример использования:

python
@log_args
def add(a, b):
    return a + b
add(2, 3)
add(5, 7)
"""

import logging

handlers = [logging.FileHandler('log.log'),
            logging.StreamHandler()]
logging.basicConfig(handlers=handlers,
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def log_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Args: {args}, kwargs: {kwargs}, result {result}")
        return result
    return wrapper


@log_args
def add(a, b, **kwargs):
    return a + b


add(2, 3, x=5)
add(5, 7, y=10)
