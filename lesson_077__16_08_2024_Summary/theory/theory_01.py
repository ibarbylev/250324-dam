"""
KISS: https://ru.wikipedia.org/wiki/KISS_(%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF)
DRY: https://ru.wikipedia.org/wiki/Don%E2%80%99t_repeat_yourself
TDD: https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0_%D1%87%D0%B5%D1%80%D0%B5%D0%B7_%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5

"""


def power_3(x):
    return x ** 3


if __name__ == "__main__":
    # create

    assert power_3(3) == 27, 'Ошибка!'
    assert power_3(-3) == -27, 'Ошибка!'

    # delete

    print('Тесты успешно пройдены')


