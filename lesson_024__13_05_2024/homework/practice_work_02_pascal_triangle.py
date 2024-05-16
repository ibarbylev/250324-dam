"""Делаем так, чтобы треугольник Паскаля был выровнен по центру,
т.е. был симметричен относительно вертикальной оси, проходящей через единицу на самой первой строке.
"""
from math import factorial as f


def bk(n, k):
    return f(n) // (f(k) * f(n - k))


def pascal_triangle(num):
    max_n: int = bk((num - 1), (num - 1) // 2)
    width: int = len(str(max_n)) + 1
    width_row: int = width * num

    text = ''
    for n in range(num):
        row = ''
        for k in range(n + 1):
            row += str(bk(n, k)).rjust(width)
        text += row.center(width_row) + '\n'

    with open("triangle_pascale.txt", "w", encoding="utf-8") as f:
        print(f.write(text))


pascal_triangle(20)
