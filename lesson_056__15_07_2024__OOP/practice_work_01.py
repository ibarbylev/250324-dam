"""Создать класс Person, каждый экземпляр которого содержит атрибут name.
И далее создать экземпляры этого класса: Том и Боб.

"""


class Person:
    def __init__(self, name):
        self.name = name


tom = Person("Tom")
bob = Person("Bob")


names = [tom, bob]

for name in names:
    print(name.name)