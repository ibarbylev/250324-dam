"""Дан массив целых чисел длины 1 и более.
Написать функцию, которая возвращает массив длины 2,
состоящих из первого и последнего элемента входного массива.

[1] -> [1, 1]
[1, 2, 3] -> [1, 3],
[7, 4, 6, 2] -> [7, 2]
"""


def return_fist_and_last(lst: list[int]) -> list[int]:
        return [lst[0], lst[-1]]


print(return_fist_and_last([1]))            # [1, 1]
print(return_fist_and_last([1, 2, 3]))      # [1, 3]
print(return_fist_and_last([7, 4, 6, 2]))   # [7, 2]
