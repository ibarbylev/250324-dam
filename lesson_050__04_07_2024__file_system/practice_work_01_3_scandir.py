"""Пишем программу, которая обходит директорию и выводит информацию в формате,
максимально похожем на ls в linux/macos (dir в windows).
Делаем то же самое для директории и всех вложенных директорий.
"""

import os


def list_directory_with_scandir(path, indent_level=0):
    """Рекурсивный обход директории и вывод информации."""
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_dir():
                    print(f"[DIR]  {entry.name}/")
                    list_directory_with_scandir(entry.path, indent_level + 4)
                else:
                    size = entry.stat().st_size
                    print(f"{' ' * indent_level}[FILE]  {size:10}  {entry.name}")
    except PermissionError:
        print(f"{' ' * indent_level}PermissionError: Cannot access '{path}'")


list_directory_with_scandir(".")
