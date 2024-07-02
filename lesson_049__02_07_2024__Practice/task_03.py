"""У вас есть текстовый файл names.txt, где каждая строка - имя человека.
Написать программу, которая выводит следующее приветствие:
    “Привет, <имя 1>, <имя 2>,... <имя n> и добро пожаловать!”.
Программу реализовать с помощью генератора и суб-генератора, где
    - суб-генератор возвращает имена из файла,
    - а основной генератор в нужный момент считывает и возвращает значения из суб-генератора.
"""
from typing import Iterator


def gen_read_file(filename) -> Iterator[str]:
    with open(filename, encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def gen_main(filename) -> Iterator[str]:
    yield "Привет"
    yield from gen_read_file(filename)
    yield "и добро пожаловать!"


print(f"{', '.join([x for x in gen_main("names.txt")])}")
# Привет, Alice, John, Max, Maria, и добро пожаловать!
