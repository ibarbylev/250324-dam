"""В функцию передаются длинная строка и длинный список.
Надо вставить элементы из списка в строку следующим образом:
 - для каждого элемента случайно определить позицию для вставки
 - и вставить этот элемент по индексу.

Решите задачу методами для строк и методами для списков.
"""

from random import randint

# print(help(randint))


def insert_list_items_into_string(text: str, lst: list[str]) -> str:
    text_list = list(text)
    for item in lst:
        pos = randint(0, len(text_list))
        text_list.insert(pos, item)
    return ''.join(text_list)


text_ex = "В функцию передаются длинная строка и длинный список"
list_ex = ['1', '2', '3', '4', '5']
print(insert_list_items_into_string(text_ex, list_ex))
