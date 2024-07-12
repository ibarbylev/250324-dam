"""Дано 3 списка:
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
list_3 = [10, 20, 30, 40]

Необходимо получить итоговый список строковых значений,
состоящий из соответствующих элементов каждого списка,
объединённых нижним подчёркиванием:

1_a_10 2_b_20 3_c_30 4_d_40 0_e_0 0_f_0

Задачу необходимо решить только с помощью функции zip_longest и list comprehension.
"""
from itertools import zip_longest

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
list_3 = [10, 20, 30, 40]
data = [list_1, list_2, list_3]

new_list = [f"{a}_{b}_{c}" for a, b, c in zip_longest(*data, fillvalue=0)]
print(*new_list, sep='  ')
# 1_a_10  2_b_20  3_c_30  4_d_40  0_e_0  0_f_0
