""""
Напишите генератор, в который
 - передаются строки разной длины
 -и который возвращает строки фиксированной длины 7 символов.

Если длина переданной строки  больше 7 символов,
    то возвращаются первые 7 символов.
Если длина переданной строки меньше 7 символов,
    то недостающие символы присоединяются к строке слева в виде нулей (“abcd” -> “000abcd”).


Новое в аннотации генераторов:
https://stackoverflow.com/questions/27264250/how-to-annotate-a-generator-in-python-3
Generator[yield_type, send_type, return_type]
"""

from typing import Generator, Iterator


def gen_7_symbols() -> Generator[str, str, None]:
    str_out = " "
    while True:
        str_in = yield str_out

        # ===== variant 1 ==========
        # if len(str_in) > 7:
        #     str_out = str_in[:7]
        # else:
        #     yield str_in.rjust(7, '0')

        # ===== variant 2 ==========
        str_out = f'{str_in[:7]:>07}'


g = gen_7_symbols()
next(g)


print(g.send('123456789'))  # 1234567
print(g.send('12345'))      # 0012345


