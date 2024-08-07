"""Создайте функцию, которая принимает список чисел и использует функцию map,
чтобы преобразовать каждый элемент списка в его квадрат.
Затем программа должна использовать функцию filter,
чтобы отфильтровать только те элементы, которые являются чётными числами.
В результате программа должна вывести новый список, содержащий квадраты только чётных чисел.
"""


def process_numbers(nums: list[int]) -> list[int]:
    squared_nums = map(lambda x: (x ** 2), nums)
    even_squares = filter(lambda x: x % 2 == 0, squared_nums)
    return list(even_squares)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(numbers)
print(result)
# [4, 16, 36, 64, 100]
