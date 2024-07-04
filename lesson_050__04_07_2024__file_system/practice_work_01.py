"""Пишем программу, которая обходит директорию и выводит информацию в формате,
максимально похожем на ls в linux/macos (dir в windows).
Делаем то же самое для директории и всех вложенных директорий.


[DIR]      ./
[FILE]          1042  practice_work_01_3_scandir.py
[FILE]          1120  practice_work_01_2_listdir.py
[FILE]          1150  practice_work_02.py
[FILE]           825  practice_work_01.py
[DIR]      homework/
    [FILE]             1  homework_02.py
    [FILE]             0  homework_01.py
[DIR]      total_recall/
    [FILE]             0  task_02.py
    [FILE]             0  task_01.py
    [FILE]             0  task_03.py
[DIR]      theory/
    [FILE]           633  theory_08_os_path.py
    [FILE]           169  theory_10_pathlab.py

"""

import os


def list_directory(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)  # {os.sep} =  '/'- Posix; '\' - Windows
        print(f"[DIR]      {os.path.basename(root)}{os.sep}")
        sub_indent = ' ' * 4 * level
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f"{sub_indent}[FILE]    {size:10}  {file}")


list_directory(".")


