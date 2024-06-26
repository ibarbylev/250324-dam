"""Создайте функцию get_statistics, которая принимает текст и возвращает словарь,
ключами которого являются слова из текста,
а значениями - другой словарь с двумя ключами
    vowels и consonants,
    и значениями количества гласных и согласных в слове.

vowels = 'aeiouyAEIOUY'

Примечание: слова не должны содержать знаки препинания.

Пример:
Mark Twain: The truth has no defense against a fool determined to believe a lie.
"""
from pprint import pprint


def get_statistics(text):
    vowels = 'aeiouyAEIOUY'

    result = {}
    words = text.split()

    for word in words:
        dct = {'consonants': 0, 'vowels': 0}

        for char in word:
            if char.isalpha():
                if char in vowels:
                    dct['vowels'] += 1
                else:
                    dct['consonants'] += 1

        result[word] = dct
    return result


text = "Mark Twain: The truth has no defense against a fool determined to believe a lie."
pprint(get_statistics(text))
