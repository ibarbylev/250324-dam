"""Дана последовательность слов.
Написать функцию, которая возвращает итератор.
В этом итераторе слова из 3-х символов
необходимо перевести в верхний регистр.
При решении использовать функциональны подход.
При описании функции использовать аннотации.

Пример:
[“The”, “quick”, “brown”, “fox”] -> [“THE”, “quick”, “brown”, “FOX”]
"""


def upper_for_3_letters(words):
    pass


words = ["The", "quick", "brown", "fox"]
new_words = upper_for_3_letters(words)
print(*new_words)
# THE quick brown FOX
