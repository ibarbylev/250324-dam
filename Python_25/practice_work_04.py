"""Решить задачу "проверь, есть ли элемент в списке" без использования дополнительной памяти
сравнимого с массивом объёма с помощью бинарного поиска.
"""

from bisect import bisect_left


def binary_search(arr, target):
    index = bisect_left(arr, target)
    return index < len(arr) and arr[index] == target


# Пример использования
arr = [1, 2, 3, 5, 8, 13, 21]
print(binary_search(arr, 5))  # Вывод: True
print(binary_search(arr, 4))  # Вывод: False
