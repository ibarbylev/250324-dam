"""Изменить решение задачи 1 так,
чтобы последовательность слов вычитывалась из текстового файла,
где каждое слово было в новой строке.

Для этого сначала необходимо получить файл:
создать функцию write_file('words.json', words)
Затем - функцию для чтения файла, read_file(),
которая возвращает итератор.
Соответственно, адаптированная функция
"""
import json


def write_file(filename, words):
    pass


def read_file(filename):
    pass


def filter_long_words(words):
    pass


words = ["cat", "elephant", "dog", "tiger", "ant", "monkey", "bee", "fox"]
write_file('words.json', words)

words_iter = read_file('words.json')
filtered_words = filter_long_words(words_iter)
print(*filtered_words)
# elephant tiger monkey
