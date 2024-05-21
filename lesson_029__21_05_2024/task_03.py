""" Дан массив целых чисел длины 3. Написать функцию, которая возвращает массив,
где первый элемент становится последним:
[1, 2, 3] -> [2, 3, 1]
[5, 11, 9] -> [11, 9, 5]
"""


def the_first_shall_be_last(lst: list[int]) -> list[int]:
    #  ===== var 1 =====
    # return lst[1:] + [lst[0]]

    #  ===== var 1 =====
    return [lst[1], lst[2], lst[0]]


print(the_first_shall_be_last([1, 2, 3]))    # [2, 3, 1]
print(the_first_shall_be_last([5, 11, 9]))   # [11, 9, 5]
