"""Напишите программу, которая принимает список чисел от пользователя
и использует функцию reduce из модуля functools,
чтобы найти произведение всех чисел в списке.
Затем программа должна использовать функцию itertools.accumulate
для накопления произведений чисел в новом списке.
В результате программа должна вывести список,
содержащий накопленные произведения.
"""

import operator
from functools import reduce
from itertools import accumulate

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find the product of all elements of the list
total_product = reduce(operator.mul, numbers)
print(total_product)
# 3628800

# Get a list of accumulated works
accumulated_products = accumulate(numbers, operator.mul)
print(*accumulated_products)
# 1 2 6 24 120 720 5040 40320 362880 3628800
