"""Необходимо восстановить код, с помощью которого были "отфильтрованы" нули из этого списка:

    [0, 2, 0, 0, 4, 6] -> [2, 4, 6]

В отсутствующем фрагменте кода НЕ ДОЛЖНО быть лямбда-функции.
"""
nums = [0, 2, 0, 0, 4, 6]


def fn(x):
    if x != 0:
        return True


# ============== variant 1  ==============
# filtered_nums = filter(fn, nums)

# ============== variant 2  ==============
# filtered_nums = filter(None, nums)

# ============== variant 3  ==============
filtered_nums = filter(bool, nums)
print(list(filtered_nums))
# [2, 4, 6]
