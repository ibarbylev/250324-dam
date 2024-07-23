"""Существует функция coffee(), которая варит кофе
и если ее вызвать, то она печатает "Сварить кофе"

Создайте 4 декоратора так, чтобы в итоге каждый из них добавлял бы
к слову "кофе" следующие фразы:
    - с сахаром,
    - с молоком
    - с сахаром и молоком
    - двойной

Вызов декорируемой функции с декоратором (с декораторами)
в итоге должен выводить печатать то, с чем именно кофе сварено

Сварить кофе двойной с сахаром и молоком
Сварить кофе с сахаром и молоком
Сварить кофе с молоком

и так далее.

"""


def with_sugar(func):
    def wrapper():
        func()
        print("с сахаром", end=' ')
    return wrapper


def with_milk(func):
    def wrapper():
        func()
        print("с молоком", end=' ')
    return wrapper


def with_sugar_and_milk(func):
    def wrapper():
        func()
        print("с сахаром и молоком", end=' ')
    return wrapper


def double_coffee(func):
    def wrapper():
        func()
        print("двойной", end=' ')
    return wrapper


@with_milk
@with_sugar
@double_coffee
def coffee1():
    print("Сварить кофе", end=' ')


@with_sugar
@double_coffee
def coffee2():
    print("Сварить кофе", end=' ')


@with_sugar_and_milk
def coffee3():
    print("Сварить кофе", end=' ')


coffee1()
print()

coffee2()
# print()

coffee3()
print()

# Сварить кофе двойной с молоком
# Сварить кофе двойной с сахаром
# Сварить кофе с сахаром и молоком
