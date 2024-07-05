"""Напишите программу, которая принимает в качестве аргумента командной строки
путь к директории и выводит список всех файлов и поддиректорий внутри этой директории.
Для этой задачи используйте модуль os и его функцию walk.
Программа должна выводить полный путь к каждому файлу и директории.
"""
import os
import sys


path = sys.argv[1]
for root, dirs, files in os.walk(path):
    for dr in dirs:
        print('[DIR]:  ', os.path.join(root, dr))
    for file in files:
        print('[FILE]: ', os.path.join(root, file))


"python homework_02.py .."
