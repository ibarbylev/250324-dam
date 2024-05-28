"""Подумайте, как уменьшить количество кода в решении задачи 2, например,
избавившись от явных циклов и использовать python comprehension вместо них.
"""

from typing import Callable


def transform(text: str, actions: list[tuple[int, Callable[[int], str]]]) -> str:
    words = text.split()
    new_words = []


    return ' '.join(new_words)


print(transform(
    text="The fast brown fox jumps over the lazy dog and hides in its hole",
    actions=[
        (2, lambda x: '--'),
    ]
))

