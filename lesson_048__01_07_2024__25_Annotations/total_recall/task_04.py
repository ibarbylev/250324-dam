"""К самой первой  задаче (# 1) добавьте новое условие:
Если число отрицательное, то оно возводится в третью степень
"""


def square_generator():
    x = 0
    while True:
        next_one = yield x
        if next_one is None:
            next_one = 1

        if next_one < 0:
            x = next_one ** 3
        else:
            x = next_one ** 2


gen = square_generator()
# Инициализация генератора
next(gen)

print(gen.send(3))   # 9
print(gen.send(-4))  # -64
print(next(gen))     # 1
print(next(gen))     # 1
print(gen.send(-5))  # -125
