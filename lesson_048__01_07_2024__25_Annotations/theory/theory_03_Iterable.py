from typing import Iterable


def generate_numbers(n: int) -> Iterable[int]:
    for i in range(n):
        yield i
