"""Выполнить задание из прошлого урока с использованием функций:
Во входном файле задаётся число. Необходимо в выходной файл вывести треугольник Паскаля,
который будет занимать верхний левый угол.
Воспользуйтесь расчётом биномиального коэффициента в цикле.
"""
from math import factorial as f


def bk(n, k):
    return f(n) // (f(k) * f(n - k))


def pascal_triangle(num):
    max_n: int = bk((num - 1), (num - 1) // 2)
    width: int = len(str(max_n)) + 1
    print(width)

    text = ''
    for n in range(num):
        row = ''
        for k in range(n + 1):
            row += str(bk(n, k)).rjust(width)
        text += row + '\n'

    with open("triangle_pascale.txt", "w", encoding="utf-8") as f:
        print(f.write(text))


pascal_triangle(20)
