"""Подумайте, как уменьшить количество кода в решении задачи 2, например,
избавившись от явных циклов и использовать python comprehension вместо них.
"""

from typing import Callable


def transform(text: str, actions: dict[int: Callable[[int], str]]) -> str:
    words = text.split()

    # =================================
    # new_words = []
    # for word in words:
    #     length = len(word)
    #     new_word = word
    #
    #     if length in actions:
    #         new_word = actions[length](word)
    #
    #     new_words.append(new_word)
    # # =================================

    new_words = [actions[len(w)](w) if len(w) in actions else w for w in words]

    return ' '.join(new_words)


print(transform(
    text="The fast brown fox jumps over the lazy dog and hides in its hole",
    actions={
        2: lambda x: '--',
        3: lambda x: x.upper(),
        4: lambda x: '****',
    }
))

