"""Добавьте в генератор square_generator() обработку исключений ValueError и GeneratorExit.
И корректно обработайте эти исключения в основном коде.

Исключение ValueError передаётся в генератор с помощью метода throw().
При получении этого исключения, генератор должен вывести на печать фразу:
    "Исключение успешно обработано!"
И затем продолжить свою обычную работу.

Исключение GeneratorExit вызывается методом close().
"""


def square_generator():
    x = 0
    while True:
        try:
            next_one = yield x
            if next_one is None:
                next_one = 1
            x = next_one ** 2
        except ValueError as e:
            print(f'ValueError, {e}')
            print('Исключение успешно обработано!')
        except GeneratorExit as e:
            print(f"GeneratorExit, {e}")
            break


gen = square_generator()
next(gen)
print(gen.send(3))  # 9
print(gen.send(4))  # 16

# Вброс исключения ValueError в генератор

print("gen.throw", gen.throw(ValueError("Throw an exception into the generator")))  # 1


print(next(gen))    # 1
print(gen.send(3))  # Output: 9

# Закрытие генератора
gen.close()

