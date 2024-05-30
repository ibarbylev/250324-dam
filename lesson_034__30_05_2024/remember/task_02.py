"""Дана функция numbers_squared.
Перепишите её как лямбда-функцию numbers_squared_lambda.
"""


def numbers_squared(lst: list[int]) -> list[int]:
    new_lst = []
    for item in lst:
        new_lst.append(item ** 2)

    return new_lst


print(numbers_squared([1, 2, 3]))   # [1, 4, 9]

# ============ variant 1 ================
numbers_squared_lambda = lambda lst: list(map(lambda x: x ** 2, lst))
print(numbers_squared_lambda([1, 2, 3]))

# ============ variant 2 ================
numbers_squared_lambda = lambda lst: [x ** 2 for x in lst]
print(numbers_squared_lambda([1, 2, 3]))