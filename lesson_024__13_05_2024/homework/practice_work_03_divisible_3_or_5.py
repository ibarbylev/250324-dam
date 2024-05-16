"""Напишите программу, которая принимает список чисел и возвращает сумму всех чисел, кратных 3 или 5.
Используйте функцию для проверки кратности.
Выведите результат на экран с помощью команды print.

Пример вывода:
Список чисел: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Сумма чисел, кратных 3 или 5: 33
"""


def is_divisible_3_or_5(x: int) -> bool:
    return x % 5 == 0 or x % 3 == 0


def sum_o_numbers_divisible_by_3_or_5(seq: list):
    amount = 0
    for num in seq:
        if is_divisible_3_or_5(num):
            amount += num
    return amount


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_o_numbers_divisible_by_3_or_5(lst)
print(f"Сумма чисел, кратных 3 или 5: {result}")
