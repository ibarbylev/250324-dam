"""Реализовать класс Counter, который представляет счётчик.
Класс должен поддерживать следующие операции:
    - Увеличение значения счётчика на заданное число (оператор +=)
    - Уменьшение значения счётчика на заданное число (оператор -=)
    - Преобразование счётчика в строку (метод __str__)
    - Получение текущего значения счётчика (метод __int__)
"""


class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other.value
        return Counter(self.value)

    def __sub__(self, other):
        self.value -= other.value
        return Counter(self.value)

    def __int__(self):
        return self.value

    def __str__(self):
        return f"Counter({self.value})"


count = Counter(10)
count7 = Counter(7)
count3 = Counter(3)

print(count)

count += count3
print(count)

count -= count7
print(count)

print('int(count) =', int(count))
