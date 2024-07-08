"""Вывести на экран все файлы и папки в заданной директории (на уровень выше текущей).
(без рекурсивного обхода всех папок)

Например:
[FILE]   ../practice_work_01.py
[DIR]    ../homework
[DIR]    ../total_recall
[DIR]    ../theory
"""

import os


def list_directory(path):
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"[DIR]    {item_path}")
        else:
            print(f"[FILE]   {item_path}")


list_directory('..')
