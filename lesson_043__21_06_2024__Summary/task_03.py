"""Имеется упорядоченный словарь ord_dict =
 OrderedDict({'orange': 2, 'apple': 5, 'banana': 2})

Также имеется готовый код, который сортирует этот список:
 - по значениям в обратном порядке;
 - и затем по алфавиту.

 Пример:
 OrderedDict({'apple': 5, 'banana': 2, 'orange': 2})

Сейчас этот код не работает, так как кто-то случайно удалил из него одну строку.
Пожалуйста, восстановите эту строку!
"""
from collections import OrderedDict

ord_dict = OrderedDict({"orange": 2, "apple": 5, "banana": 2})
print(ord_dict)   # OrderedDict({'orange': 2, 'apple': 5, 'banana': 2})

new_ord_dict = OrderedDict(
    # Здесь отсутствует одна строка кода:
)
print(new_ord_dict)   # OrderedDict({'apple': 5, 'banana': 2, 'orange': 2})
