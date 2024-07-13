"""Создайте класс Student для представления студента.
Класс должен иметь атрибуты
    - name (имя) и
    - age (возраст),
а также метод display_info(), который выводит информацию о студенте.

Затем создайте экземпляр класса Student с заданным именем и возрастом
и вызовите метод display_info().
"""


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'

    def display_info(self):
        print(self.__str__())


student = Student('John', 20)
student.display_info()
