"""Дан список, упорядоченный по возрастанию.
Определите, сколько в нём различных элементов.
Не допускается использование set()
[1, 2, 2, 3, 3, 3] -> 3
[1, 1, 1, 1, 1] -> 1
[] -> 0
"""


def count_uniq_items(nums: list[int]) -> int:

    return 0


print(count_uniq_items([1, 2, 2, 3, 3, 3]))  # 3
print(count_uniq_items([1, 1, 1, 1, 1, 1]))  # 1
print(count_uniq_items([]))                  # 0
