"""Нужно создать свои исключения на каждый тип ошибки.
При обнаружении ошибки бросается исключение с причиной ошибки,
например, “возраст меньше 18 лет (дата рождения такая-то)”
или “номер банковского счета неверен: когда страны “SR” не существует”.

Ознакомьтесь с тем, что такое IBAN и реализуйте проверку нескольких правил формата (страна, длина).

IBAN должен соответствовать стандарту длины (начинаться с кода страны и содержать правильное количество символов)
https://en.wikipedia.org/wiki/International_Bank_Account_Number

Решение должно использовать исключения и итераторы.

PS
Параметры IBAN в значительной степени зависят от страны-нахождения банка.
Поэтому для простоты считаем, что все счета - только из Германии.
Например, IBAN: DE89370400440532013000
Проверяем:
 - длина (после удаления внутренних пробелов) - 22 символа
 - первые 2 символа - буквы
 - остальные 20 символов - цифры

"""
from task_01 import users



class IBANException(Exception):
    pass


def iban_validation(iban: str) -> bool:
    mistakes = []
    iban_corr = iban.replace(" ", "")

    if len(iban_corr) != 22:
        mistakes.append("Incorrect Length of IBAN!")

    if not iban_corr[:2].isalpha():
        mistakes.append("The first two characters must be letters!")

    if not iban_corr[2:].isdigit():
        mistakes.append("The last twenty characters must be digits!")

    if mistakes:
        raise IBANException("; ".join(mistakes))
    return True


for user in users:
    try:
        print(iban_validation(user[3]))

    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')


# True
# IBANException: Incorrect Length of IBAN!
# True
# IBANException: The first two characters must be letters!
# IBANException: The last twenty characters must be digits!
# IBANException: Incorrect Length of IBAN!; The first two characters must be letters!; The last twenty characters must be digits!
# IBANException: Incorrect Length of IBAN!
