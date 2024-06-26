"""Задача на наибольший общий делитель

Найти максимальное целое число, на которое без остатка делятся числа a и b.

Метод Эвклида - это алгоритм для нахождения наибольшего общего делителя (НОД) двух целых чисел.
Этот метод основан на следующем простом наблюдении:
НОД(a, b) равен НОД(b, a % b), где % обозначает операцию взятия остатка от деления.
"""


def gcd_loop(a, b):
    print(a, b)
    while b:
        a, b = b, a % b
        print(a, b)
    return a


num2 = 48
num1 = 18
print(f"Наибольший общий делитель чисел {num1} и {num2}: {gcd_loop(num1, num2)}")
