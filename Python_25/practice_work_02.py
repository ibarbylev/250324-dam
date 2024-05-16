"""Напишите функцию, которая принимает список строк и возвращает наибольшую строку из списка.
Функция должна быть аннотирована с помощью аннотаций типов.
"""


def get_longest_item(lines):
    return max(lines, key=lambda x: len(x))


print(get_longest_item(['aaa', 'b', 'cccd', 'dd']))
