"""Дан генератор, содержащий последовательность слов words.
Вернуть предложение, составленное из слов данной последовательности.
Слова в полученном предложении разделены пробелами.
При описании генератора использовать аннотации.

"""
from typing import Generator, List


def gen(lst: List[str]) -> Generator[str, None, None]:
    yield from lst


words = ["This", "is", "a", "simple", "sentence"]

words_string = " ".join(gen(words))
print(words_string)
# This is a simple sentence
