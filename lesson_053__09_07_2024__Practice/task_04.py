"""Изменить решение задачи 1 так,
чтобы последовательность слов вычитывалась из текстового файла,
где каждое слово было в новой строке.

Для этого сначала необходимо получить файл:
создать функцию write_file('words.json', words)
Затем - функцию для чтения файла, read_file(),
которая возвращает итератор.
Соответственно, адаптированная функция
"""
from typing import Iterator, List
import json


def write_file(filename: str, words: List[str]) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(words, f, indent=4)


def read_file(filename: str) -> Iterator[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        return iter(json.load(f))


def filter_long_words(word_list: Iterator[str]) -> Iterator[str]:
    return filter(lambda word: len(word) > 3, word_list)


words = ["cat", "elephant", "dog", "tiger", "ant", "monkey", "bee", "fox"]
write_file('words.json', words)

words_iter = read_file('words.json')
# print(type(words_iter))
filtered_words = filter_long_words(words_iter)

print(*filtered_words, sep='\n')
# elephant
# tiger
# monkey
