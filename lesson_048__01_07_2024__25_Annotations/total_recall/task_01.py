"""Создайте бесконечный генератор square_generator(),
который принимает целое число и возвращает его квадрат.
"""


def square_generator():
    x = 0
    while True:
        next_one = yield x
        x = next_one * next_one


gen = square_generator()
next(gen)

print(gen.send(3))  # 9
print(gen.send(4))  # 16
print(gen.send(5))  # 25


