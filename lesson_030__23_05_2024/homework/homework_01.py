"""Напишите программу, которая принимает матрицу (вложенный список) от пользователя
и находит сумму всех элементов в матрице.
Используйте вложенные списки и циклы для обхода элементов матрицы.

Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Пример вывода:
Сумма элементов в матрице: 45

"""


def total_sum(nums: list[list[int]]) -> None:
    amount = 0
    for row in nums:
        for n in row:
            amount += n

    print(f"Сумма элементов в матрице: {amount}")


total_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])