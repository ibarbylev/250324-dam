"""Напишите генератор, который будет генерировать арифметическую прогрессию

    В качестве аргументов генераторной функции передается:
        - начальное значение прогрессии,
        - шаг (по умолчанию = 1),
        - и последний элемент прогрессии (по умолчанию бесконечная прогрессия)
"""


def gen_arithmetic_progression(start, step=1, end=None):
    current = start
    if end is None:
        while True:
            yield current
            current += step
    else:
        while current <= end:
            yield current
            current += step


print(" ----- infinity progression -----")
gen = gen_arithmetic_progression(0, 2)
for _ in range(10):
    print(next(gen))


print(" ----- finite progression-----")

gen = gen_arithmetic_progression(1, 3, 10)
for value in gen:
    print(value)