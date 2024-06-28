"""Создайте бесконечный генератор арифметической прогрессии.
 По умолчанию он начинается с 0 и его шаг равен 5.

Генератор может изменить свой шаг в процессе работы,
если новое значение отправлено в него с помощью метода send.
"""


def gen_arithmetic_progression(start=0, step=5):
    pass


g = gen_arithmetic_progression()
print(next(g))  # 0
print(next(g))  # 5
print(g.send(20))  # 25
print(next(g))  # 45
print(next(g))  # 65


