"""Добавьте счётчик количества выпущенных с конвейера автомобилей count,
который должен увеличиваться на 1
при создании очередного экземпляров класса.
"""

"""Создайте класс Car для представления автомобиля.
Класс должен иметь атрибуты brand (марка) и model (модель),
которые передаются в конструкторе при создании экземпляра класса.
Реализуйте метод __str__, который будет возвращать строку
в формате "Марка: <марка>, Модель: <модель>".

Ожидаемый вывод:

Марка: Toyota, Модель: Camry
Марка: BMW, Модель: X5
"""


class Car:
    count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.count += 1

    def __str__(self):
        return f'Марка: {self.brand}, Модель: {self.model}'


print(Car.count)

car1 = Car("Toyota", "Camry")
print(car1)
print(Car.count)

car2 = Car("BMW", "X5")
print(car2)
print(Car.count)

# 0
# Марка: Toyota, Модель: Camry
# 1
# Марка: BMW, Модель: X5
# 2