from typing import Iterable


def generate_numbers(n: int) -> Iterable[int]:
    for i in range(n):
        yield i


gen = generate_numbers(3)
for x in gen:
    print(x)
