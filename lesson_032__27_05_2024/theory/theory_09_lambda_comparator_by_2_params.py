"""Сортировка по нескольким параметрам

Сортируем сначала по второму элементу, а потому по второй букве первого элемента
"""

lst = [('aa', 2), ('av', 2), ('ab', 1), ('za', 1)]
print(lst)

lst.sort(key=lambda x: (x[1], x[0][1]))
print(lst)


"""сортировка элемента по убыванию с помощью МИНУСА !!!"""
lst.sort(key=lambda x: (x[1], -ord(x[0][1])))
print(lst)