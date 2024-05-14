"""Перепишите решение следующей задачи с использованием функции.
У нас есть две логические переменные: isWeekday, isVacation (выходной день и каникулы).
Они могут принимать разные значения, всего 4 комбинации:
true - true, true - false, false - false, false - true.
Есть правило: мы можем поспать, если день не рабочий или мы на каникулах.
Напишите программу, которая в зависимости от значений двух переменных печатает, можем ли мы поспать или нет.
То есть для значений isWeekday = False и isVacation = False программа должна печатать “можете поспать”.
"""


def can_you_sleep(is_weekday: bool, is_vacation: bool) -> None:
    if not (is_weekday or is_vacation):
        word = ""
    else:
        word = "НЕ "
    print(f"{word}можете поспать")


can_you_sleep(False, False)
can_you_sleep(False, True)
can_you_sleep(True, False)
can_you_sleep(True, True)

