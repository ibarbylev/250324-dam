"""Создать функцию get_total_statistics, которая
 - принимает текст
 - и возвращает словарь в формате <буква: её количество в тексте>.

Перед начало работы текст необходимо перевести в нижний регистр.
"""
from pprint import pprint

text = 'Bernard Shaw: "Life isn\'t about finding yourself. Life is about creating yourself."'


def get_total_statistics(text):
    dct = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            dct[char] = dct.get(char, 0) + 1

    return dct


pprint(get_total_statistics(text))
# {'a': 5,
#  'b': 3,
#  'c': 1,
#  'd': 2,
#  'e': 6,
#  'f': 5,
#  'g': 2,
#  'h': 1,
#  'i': 7,
#  'l': 4,
#  'n': 5,
#  'o': 4,
#  'r': 5,
#  's': 5,
#  't': 4,
#  'u': 4,
#  'w': 1,
#  'y': 2}
