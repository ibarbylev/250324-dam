"""Дана последовательность слов. Написать функцию,
которая возвращает итератор последовательности слов,
длина которых больше трёх символов.
Использовать lambda-функции и filter.
При описании функции использовать аннотации.
"""
from typing import Iterator, List


def filter_long_words(word_list: List[str]) -> Iterator[str]:
    return filter(lambda word: len(word) > 3, word_list)
    # return filter(lambda x: len(x) > 3, word_list)
    # return filter(lambda word: len(word)>3, word_list)

# Пример использования функции
words = ["cat", "elephant", "dog", "tiger", "ant", "monkey", "bee", "fox"]
filtered_words = filter_long_words(words)
print(*filtered_words)
# elephant tiger monkey
