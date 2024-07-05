"""Создайте функцию find_py_file(), которая
 - обходит заданную директорию и её поддиректории,
 - находит все файлы с расширением .py,
 - и выводит их относительные пути и размеры
                        file_size = os.path.getsize(file_path)
"""

import os


def find_py_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                pass


find_py_files('.')

# ./task_02.py 662
# ./task_01.py 503
# ./task_04.py 1182
# ./task_06.py 1526
# ./task_05.py 824
# ./task_03.py 1233
# ./task_09.py 1537
# ./task_08.py 307
# ./task_07.py 488
