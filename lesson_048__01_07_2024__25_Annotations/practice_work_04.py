"""Решить задачу "проверь, есть ли элемент в списке"
без использования дополнительной памяти
сравнимого с массивом объёма с помощью бинарного поиска.

Важно: бинарный поиск работает только на отсортированных списках.
Следовательно, сначала мы должны отсортировать список и только затем выполнить бинарный поиск.
Сортировка списка потребует O(n log n) времени, но это не требует дополнительной памяти
сравнимого объёма с массивом.
После этого сам бинарный поиск выполняется за O(log n) времени.
"""


def binary_search(a):
    pass


def contains_element():
    pass


lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(contains_element(lst, 5))  # Вывод: True
print(contains_element(lst, 7))  # Вывод: False