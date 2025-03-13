from typing import Iterable


def generate_numbers(n: int) -> Iterable[int]:
    for i in range(n):
        yield i


def generate_numbers_2(n: int) -> Iterable[str]:
    for char in ['a', 'b', 'b']:
        yield char


g = generate_numbers(10)
for item in g:
    print(item)
