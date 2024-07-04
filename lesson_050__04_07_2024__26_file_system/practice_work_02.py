"""Напишите программу, которая принимает в качестве аргумента командной строки
 путь к директории и выводит список всех файлов с расширением .txt
 внутри этой директории и ее поддиректорий.
Для этой задачи используйте рекурсивную функцию, которая будет обходить
все поддиректории и искать файлы с расширением .txt.
"""
import os


def get_all_txt_files(path, indent_level=0):
    pass


start_directory = os.path.abspath('..')
print('start_directory: ', start_directory)
get_all_txt_files(start_directory)
