"""Создайте список из 10 объектов этого класса,
описывающих модели разных марок, лет и цветов.
Используйте для этого следующие данные:
"""

from task_01 import Car

data = [
    ('Golf', 2020, 'Red'),
    ('Toyota', 2019, 'Blue'),
    ('Polo', 2021, 'Green'),
    ('Alfa-Romeo', 2018, 'Black'),
    ('Skoda', 2022, 'Red'),
    ('Touareg', 2017, 'Yellow'),
    ('Sharan', 2016, 'Red'),
    ('Phaeton', 2015, 'Gold'),
    ('BMV', 2014, 'Brown'),
    ('Nissan', 2013, 'Red')
]

# cars = [Car(model, year, color) for model, year, color in data]
cars = [Car(*car) for car in data]


if __name__ == '__main__':
    for car in cars:
        print(car)
