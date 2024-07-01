"""Создайте бесконечный генератор square_generator(),
который принимает целое число и возвращает его квадрат.
А если ничего не передано, генератор возвращает 1.
"""


def square_generator():
    x = 0
    while True:
        next_one = yield x

        # if next_one is None:
        #     next_one = 1

        next_one = 1 if next_one is None else next_one

        x = next_one * next_one


gen = square_generator()
next(gen)

print(gen.send(3))  # 9
print(gen.send(4))  # 16
print(next(gen))    # 1
print(next(gen))    # 1
print(gen.send(5))  # 25

