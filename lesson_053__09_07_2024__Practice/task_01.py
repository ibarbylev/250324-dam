"""Дана последовательность слов. Написать функцию,
которая возвращает итератор последовательности слов,
длина которых больше трёх символов.
Использовать lambda-функции и filter.
При описании функции использовать аннотации.
"""


def filter_long_words(word_list):
    pass


# Пример использования функции
words = ["cat", "elephant", "dog", "tiger", "ant", "monkey", "bee", "fox"]
filtered_words = filter_long_words(words)
print(*filtered_words)
# elephant tiger monkey