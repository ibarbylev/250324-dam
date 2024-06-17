"""Необходимо создать функцию get_alphabet_statistics, которая
 - принимает текст
 - и возвращает словарь в формате: <буква: её количество в этом тексте>

Перед обработкой текста его необходимо перевести в нижний регистр.
"""
from pprint import pprint

text = 'Winston Churchill: "Those who never change their minds never change anything"'


def get_alphabet_statistics(text: str) -> dict[str, int]:
    dct = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            # if char in dct:
            #     dct[char] = dct[char] + 1
            # else:
            #     dct[char] = 1
            dct[char] = dct.get(char, 0) + 1

    return dct


pprint(get_alphabet_statistics(text))
# {'a': 3,
#  'c': 4,
#  'd': 1,
#  'e': 8,
#  'g': 3,
#  'h': 8,
#  'i': 5,
#  'l': 2,
#  'm': 1,
#  'n': 9,
#  'o': 3,
#  'r': 4,
#  's': 3,
#  't': 4,
#  'u': 1,
#  'v': 2,
#  'w': 2,
#  'y': 1}
