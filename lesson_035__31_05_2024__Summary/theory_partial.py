from functools import partial


def multiply(x, y):
    return x, y


# Создание новой функции, которая всегда будет использовать аргумент x = 2
multiply_by_two = partial(multiply, 2)

# Создание другой функции, которая всегда будет использовать аргумент y = 2
multiply_by_two_var2 = partial(multiply, y=2)

result = multiply_by_two(5)
print(result)  # Выводит 10
result = multiply_by_two_var2(5)
print(result)  # Выводит 10
