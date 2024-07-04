"""Пишем программу, которая обходит директорию и выводит информацию в формате,
максимально похожем на ls в linux/macos (dir в windows).
Делаем то же самое для директории и всех вложенных директорий.
"""

import os


def list_directory_with_listdir(path, indent_level=0):
    """Рекурсивный обход директории с помощью os.listdir и вывод информации."""
    try:
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"{' ' * indent_level}[DIR]  {item}{os.sep}")
                list_directory_with_listdir(item_path, indent_level + 4)
            else:
                size = os.path.getsize(item_path)
                print(f"{' ' * indent_level}[FILE]  {size:10}  {item}")
    except PermissionError:
        print(f"{' ' * indent_level}PermissionError: Cannot access '{path}'")


list_directory_with_listdir(".")
