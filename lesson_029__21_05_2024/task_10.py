"""Дан список, упорядоченный по возрастанию.
Определите, сколько в нём различных элементов.
Не допускается использование set()
[1, 2, 2, 3, 3, 3] -> 3
[1, 1, 1, 1, 1] -> 1
[] -> 0
"""


def count_uniq_items(nums: list[int]) -> int:
    # ================ var 1  ===============
    # return len(set(nums))

    # ================ var 2  ===============
    if not nums:
        return 0
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            count += 1

    return count


print(count_uniq_items([1, 2, 2, 3, 3, 3]))  # 3
print(count_uniq_items([1, 1, 1, 1, 1, 1]))  # 1
print(count_uniq_items([1]))                 # 1
print(count_uniq_items([]))                  # 0
