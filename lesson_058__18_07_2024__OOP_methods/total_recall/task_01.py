"""Создайте класс Animal с методами eat() и run().
Наследуйте от него классы Cat и класс Dog.
Эти классы должны иметь
 - атрибут name
 - и методы eat() и run().
При вызове методов eat() и run() соответственно выводится на печать:
"Кот Рыжик ест"
"Кот Рыжик бегает"
"Собака Шарик ест"
"Собака Шарик бегает"
"""


class Animal:
    pass


class Cat:
    pass


class Dog:
    pass


if __name__ == '__main__':
    cat_ryzhik = Cat("Рыжик")
    dog_sharik = Dog("Шарик")

    cat_ryzhik.eat()
    cat_ryzhik.run()
    dog_sharik.eat()
    dog_sharik.eat()

# Кот Рыжик ест.
# Кот Рыжик бегает.
# Собака Шарик ест.
# Собака Шарик ест.
