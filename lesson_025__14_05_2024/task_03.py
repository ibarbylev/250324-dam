"""Даны два целых числа A и B (при этом A ≤ B).
Напишите функцию, которая печатает все числа от A до B включительно (в одну строку через пробел).
"""


def range_between_a_and_b(a: int, b: int) -> None:
    # -------- var 1 ---------
    # result = ""
    # for i in range(a, b + 1):
    #     result += str(i) + " "
    # print(result)

    # -------- var 2 ---------
    # for i in range(a, b + 1):
    #     print(i, end=" ")

    # -------- var 3 ---------
    print(*range(a, b+1))  # [5, 6, 7, 8, 9, 10]


range_between_a_and_b(5, 10)
