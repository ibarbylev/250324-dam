"""Напишите программу, которая принимает в качестве аргумента
командной строки путь к файлу 'example.py' и запускает его.
При запуске файла программа должна выводить сообщение
"Файл <имя файла> успешно запущен".
Если файл не существует или не может быть запущен,
программа должна вывести соответствующее сообщение об ошибке.
"""

import os
import sys

try:
    # print(sys.argv)
    filename = sys.argv[1]
    os.system(f'python {filename}')
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не существует")
    print(f"Файл <{filename}> успешно запущен")

except IndexError as e:
    print(f"Похоже, что вы не указали исполняемый файл \n{e.__class__.__name__}: {e}")
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
