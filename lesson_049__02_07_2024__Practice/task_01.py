"""Напишите бесконечный генератор, который возвращает последовательность целых чисел,
где каждое следующее больше предыдущего в 2 раза.
"""
from typing import Iterator


def gen_double_num(start: int = 1) -> Iterator[int]:
    num = start
    while True:
        yield num
        num *= 2


gen = gen_double_num()
for _ in range(10):
    print(next(gen))
