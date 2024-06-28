"""Даны два файла с целыми числами в каждой строке.
Необходимо найти сумму всех чисел в файле.
Начните с "маленького". Получилось? Отлично.
Теперь опробуйте то же самое сделать с большим…
"""


# from random import randint
#
#
# def write_file(filename, n_max):
#     with open(filename, 'w', encoding='utf-8') as file:
#         for _ in range(n_max):
#             file.write(f'{randint(0, n_max)}\n')
#
#
# # write_file('huge_file.txt', 1000000000)


def get_sum_nums_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        return sum([int(n) for n in file])


print(get_sum_nums_from_file('huge_file.txt'))
# print(get_sum_nums_from_file('small_file.txt'))
