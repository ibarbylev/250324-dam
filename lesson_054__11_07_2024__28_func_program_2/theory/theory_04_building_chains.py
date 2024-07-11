"""Предположим, нам необходимо сложить сумму квадратов всех чётных чисел в списке"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
print(result)
# Результат: 20

""" ====================== variant 2 ======================= 
попробуем сделать код более читабельным
"""
sum_of_sq = map(lambda x: x ** 2, numbers)
filtered_sq = filter(lambda x: x % 2 == 0, sum_of_sq)
sum_of_sq_even = reduce(lambda x, y: x + y, filtered_sq)
print(sum_of_sq_even)
