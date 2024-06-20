"""Создать функцию get_statistics_by_words, которая
 - принимает текст
 - и возвращает словарь в формате <буква: [её количество в каждом слове, где есть хотя бы одна]>.

Перед начало работы текст необходимо перевести в нижний регистр.
"""
from pprint import pprint

text = 'Bernard Shaw: "Life isn\'t about finding yourself. Life is about creating yourself."'


def get_statistics_by_words(text):
    dct = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            # dct[char] = dct.get(char, 0) + 1
            dct.setdefault(char, []).append(1)
            # dct[char] = dct.setdefault(char, 0) + 1
    return dct


pprint(get_statistics_by_words(text))
# {'a': [1, 1, 1, 1, 1],
#  'b': [1, 1, 1],
#  'c': [1],
#  'd': [1, 1],
#  'e': [1, 1, 1, 1, 1, 1],
#  'f': [1, 1, 1, 1, 1],
#  'g': [1, 1],
#  'h': [1],
#  'i': [1, 1, 2, 2, 1, 1, 1],
#  'l': [1, 1, 1, 1],
#  'n': [1, 1, 2, 2, 1],
#  'o': [1, 1, 1, 1],
#  'r': [2, 2, 1, 1, 1],
#  's': [1, 1, 1, 1, 1],
#  't': [1, 1, 1, 1],
#  'u': [1, 1, 1, 1],
#  'w': [1],
#  'y': [1, 1]}
