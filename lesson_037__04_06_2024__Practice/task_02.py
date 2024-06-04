"""Дано натуральное число N.
Написать функцию power_of_2(N), которая
    - печатает слово YES, если число N является точной степенью двойки
      (2^0 = 1,
       2^1 = 2,
       2^2 = 4,
       2^3 = 8 и так далее)
    - или слово NO в противном случае.

Пользуемся рекурсией, а операцией возведения в степень не пользуемся.

Пример:
    power_of_2(8) вернет YES,
    power_of_2(1) вернет YES.
    power_of_2(3) вернет NO.
"""


def power_of_2(n):
    if n == 1:
        return "YES"
    elif n % 2 != 0 or n == 0:
        return "NO"
    else:
        return power_of_2(n // 2)


print(power_of_2(8))  # YES
print(power_of_2(1))  # YES
print(power_of_2(3))  # NO

