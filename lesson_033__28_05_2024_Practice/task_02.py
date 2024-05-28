"""Изменим условие 1 задачи:
нужно, чтобы функция из примера 1 могла также менять слова длины 4 на написанные маленькими буквами.
В общем виде, нужно, чтобы функции можно было дать условие, которому соответствует указанное действие.

Например, все слова длины 4 хотим заменить на звёздочки.
А слова длины 2 - на чёрточки.
Каждое выполнение функции - одно условие и одно действие.
"""

from typing import Callable


def transform(text: str, actions: dict[int: Callable[[int], str]]) -> str:
    words = text.split()
    new_words = []
    for word in words:
        length = len(word)
        new_word = word

        if length in actions:
            new_word = actions[length](word)

        new_words.append(new_word)

    return ' '.join(new_words)


print(transform(
    text="The fast brown fox jumps over the lazy dog and hides in its hole",
    actions={
        2: lambda x: '--',
        3: lambda x: x.upper(),
        4: lambda x: '****',
    }
))
