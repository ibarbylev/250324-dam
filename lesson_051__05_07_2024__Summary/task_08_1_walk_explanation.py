"""Создайте функцию find_txt_file(), которая
 - обходит заданную директорию и её поддиректории,
 - находит все файлы с расширением .py,
 - и выводит их относительные пути и размеры
                        file_size = os.path.getsize(file_path)
"""

import os


def find_txt_files(directory):
    for root, dirs, files in os.walk(directory):
        print("root:", root)
        print("dirs:", dirs)
        print("files:", files)
        print("=========================")


find_txt_files('..')

