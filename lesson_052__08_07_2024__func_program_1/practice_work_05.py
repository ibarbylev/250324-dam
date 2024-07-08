"""Считать данные из файла anna-karenina.txt, очистить их,
оставить только слова длиной более десяти символов.
"""
from typing import Iterator


def read_file(file_path: str) -> str:
    pass


def clean_word(word: str) -> str:
    pass


def clean_and_split(text: str) -> Iterator:
    pass


def filter_long_words(words: Iterator) -> Iterator:
    pass


def process_text(file_path: str) -> Iterator:
    pass


file_path = 'anna-karenina.txt'
long_words = process_text(file_path)
print(*long_words, sep='\n')
