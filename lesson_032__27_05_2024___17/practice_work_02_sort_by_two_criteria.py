"""Напишите программу, которая сортирует список строк по длине строк с использованием метода sort().
Далее, если строки имеют одинаковую длину, то они должны быть упорядочены в лексикографическом порядке.
Программа должна выводить промежуточные этапы сортировки и итоговый отсортированный список.

Пример вывода:
Введите список строк, разделенных пробелами: apple pear banana dog cat lime
Исходный список: ['apple', 'pear', 'banana', 'dog', 'cat']
Отсортированный список по длинам строк:   ['dog', 'cat', 'pear', 'lime', 'apple', 'banana']
Отсортированный список по двум критериям: ['cat', 'dog', 'lime', 'pear', 'apple', 'banana']
"""


def sort_list_by_length_items(line: str) -> None:
    lst: list[str] = line.split()
    print(f"Исходный список: {lst}")
    lst.sort(key=lambda x: ...)
    print(f"Отсортированный список по длинам строк:   {lst}")
    lst.sort(key=lambda x: ...)
    print(f"Отсортированный список по двум критериям: {lst}")


sort_list_by_length_items("apple pear banana dog cat lime")
