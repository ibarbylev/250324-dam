"""Дан массив целых чисел.
Дать ответ на вопрос есть ли в нём два элемента, сумма которых равна нулю.

    - Решить с двумя вложенными циклами.
    - Решить с помощью множеств.

Ограничение: известно, что массив не может содержать более одного нуля.

"""


def has_zero_sum_pair_1(items):  # O(n^2)
    n = len(items)
    for i in range(n):    # O(n)
        for j in range(i + 1, n):   # O(n)
            if items[i] + items[j] == 0:
                return True
    return False


def has_zero_sum_pair_2(items):
    my_set = set()
    for item in items:   # O(n)
        if -item in my_set:   # O(1)
            return True
        my_set.add(item)
    return False


# Пример использования
arr1 = [1, 2, -1, 3, 4, 0]
arr2 = [1, 2, 1, 3, 4, 0]
print(has_zero_sum_pair_1(arr1))  # Выводит True, потому что 1 и -1 дают в сумме 0
print(has_zero_sum_pair_1(arr2))  # Выводит False

print(has_zero_sum_pair_2(arr1))  # Выводит True, потому что 1 и -1 дают в сумме 0
print(has_zero_sum_pair_2(arr2))  # Выводит False




