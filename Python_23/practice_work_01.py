"""Создать генератор, который будет делать то же самое,
что и range с одним аргументом.
"""
from typing import Generator


# ----- variant 1 ------
def gen(x):
    pass


g = gen(3)
print(isinstance(g, Generator))

for x in g:
    print(x)
