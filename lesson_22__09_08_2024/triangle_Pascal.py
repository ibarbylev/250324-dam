"""Во входном файле задаётся число.
Необходимо в выходной файл вывести треугольник Паскаля,
который будет занимать верхний левый угол.
Воспользуйтесь расчётом биномиального коэффициента в цикле.
"""
from math import factorial as f

num = 10


def bk(n, k):
    return f(n) // (f(k) * f(n - k))


text = ''
for n in range(num):
    row = ''
    for k in range(n + 1):
        row += str(bk(n, k)) + " "

    text += row + '\n'

print(text)
