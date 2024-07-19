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
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Марка {self.brand} Модель {self.model}"


car1 = Car("Toyota", "Camry")
car2 = Car("BMW", "X5")

print(car1)
print(car2)

# Марка: Toyota, Модель: Camry
# Марка: BMW, Модель: X5
