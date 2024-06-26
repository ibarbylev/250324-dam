"""На входе функция to_set() получает строку или список чисел.
Преобразуйте их в множество.
На выходе должно получиться множество и его мощность (cardinality).
"""


def to_set(seq: list[int] | str) -> tuple:
    seq = set(seq)
    return seq, len(seq)


print(to_set([1, 2, 3, 4, 5, 5]))   # ({1, 2, 3, 4, 5}, 5)
print(to_set("cardinality"))   # ({'y', 'r', 'a', 'c', 'i', 't', 'l', 'd', 'n'}, 9)
