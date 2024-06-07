"""Имеется множество my_set = {1, 2, 3}
Необходимо добавить в него элементы списка lst = [4, 5, 6],
чтобы получить результат {1, 2, 3, 4, 5, 6}.

Задание необходимо выполнить, как минимум, двумя способами.
"""

my_set = {1, 2, 3}
lst = [4, 5, 6]

# ==== variant 1 ====
#
# my_set.update(lst)
# print(my_set)

# ==== variant 2 ====
# for element in lst:
#     my_set.add(element)
#
# print(my_set)

# ==== variant 3 ====
set_2 = set(lst)
my_set = my_set | set(lst)
print(my_set)
