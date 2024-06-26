"""Напишите программу, которая принимает список чисел от пользователя и вставляет новое число в середину списка.
Затем программа должна удалить элемент из середины списка.

1.) Используйте методы insert() и remove() для вставки и удаления элементов.

2.) Попробуйте потом решить задачу без использования методов insert() и remove().

Выведите итоговый список на экран с помощью команды print.

Пример вывода:
Исходный список: [1, 2, 3, 4, 5]
Введите новое число: 10
Список после вставки: [1, 2, 10, 3, 4, 5]
Список после удаления: [1, 2, 3, 4, 5]
"""


a = [1, 2, 3, 4, 5]
idx = len(a) // 2
a.insert(idx, 10)
print(a)
a.remove(10)
print(a)


a = [1, 2, 3, 4, 5]
idx = len(a) // 2
a = a[:idx] + [10] + a[idx:]
print(a)
a = a[:idx] + a[idx+1:]
print(a)