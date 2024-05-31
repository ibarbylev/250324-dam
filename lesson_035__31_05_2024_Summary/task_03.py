"""Исправьте ошибку в коде с помощью изменения области видимости переменной x."""
x = 0


def outer_function():
    x = 1

    def inner_function():
        nonlocal x
        x += 2
    inner_function()
    print(x)  # 3


outer_function()   # 3
print(x)           # 0