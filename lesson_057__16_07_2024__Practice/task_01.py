"""Создать класс Car (машина) со следующими полями: model, year, color."""


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.model} {self.year} {self.color}"


if __name__ == '__main__':
    car = Car("a", "1", "c")
    print(car)

