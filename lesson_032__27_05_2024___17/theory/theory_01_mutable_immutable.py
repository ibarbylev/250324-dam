"""Неизменяемые типы данных, которые передаются в функцию, вынуждены создавать свои копии,
чтобы изменяться.
Изменяемые - изменяются сами.
"""


def func(lst, value):
    value += "bc"
    lst[0] = value
    return lst


nums = [1, 2, 3]
latter = 'a'
print(func(nums, latter))
print('nums =', nums)
print('latter = ', latter)

