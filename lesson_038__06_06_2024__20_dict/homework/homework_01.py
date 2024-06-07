"""Напишите функцию merge_dicts, которая принимает
произвольное количество словарей в качестве аргументов
и возвращает новый словарь, объединяющий все входные словари.
Если ключи повторяются, значения должны быть объединены в список.

Пример ввода:

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_c = {'c': 5, 'd': 6}

merge_dicts(dict_a, dict_b, dict_c)

Пример вывода:
{'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}
"""


def merge_dicts(*args: dict) -> dict[str, list]:
    my_dict = {}
    for arg in args:
        for k, v in arg.items():
            my_dict.setdefault(k, []).append(v)

    return my_dict


dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_c = {'c': 5, 'd': 6}
print(merge_dicts(dict_a, dict_b, dict_c))