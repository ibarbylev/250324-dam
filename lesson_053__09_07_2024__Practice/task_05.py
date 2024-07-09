"""Дан текстовый файл, где каждая строка описывает человека в формате
<Name>; <Age>
Sergey;35
Ivan;25
Svetlana;20
Maria;27
Напишите функцию, которая возвращает имя самого старшего человека.

Напишите ещё одну функцию так, чтобы программу возвращала
имена тех, чей возраст больше 25 лет.

При решении использовать функциональны подход.
При описании функции использовать аннотации.
"""
from typing import Iterator, Tuple


def pars_line(lines: Iterator[str]) -> Iterator[Tuple[str, int]]:
    # Sergey;35 Ivan;25 Svetlana;20 Maria;27
    return map(lambda x: (x.split(';')[0], int(x.split(';')[1])), lines)


def read_file(filename: str) -> Iterator[str]:
    with open(filename, encoding='utf-8') as f:
        return map(lambda x: x.strip(), f.readlines())


def get_the_oldest_person(data: Iterator[Tuple[str, int]]) -> Tuple[str, int]:
    # ('Sergey', 35)('Ivan', 25)('Svetlana', 20)('Maria', 27)
    return max(data, key=lambda x: x[1])


def get_persons_older_25(data: Iterator[Tuple[str, int]]) -> Iterator[str]:
    # data = ('Sergey', 35)('Ivan', 25)('Svetlana', 20)('Maria', 27)

    # ==== variant 1 ====
    older_25_iter = filter(lambda x: x[1] > 25, data)
    return map(lambda x: x[0], older_25_iter)

    # ==== variant 2 ====
    # return (p[0] for p in data if p[1] > 25)


data_iter = read_file('persons.txt')
# print(*data_iter)

# print(*pars_line(data_iter))
data = pars_line(data_iter)  # ('Sergey', 35) ('Ivan', 25) ('Svetlana', 20) ('Maria', 27)

person_name, _ = get_the_oldest_person(data)
print(f'The oldest man is {person_name}.')

data_iter = read_file('persons.txt')
data = pars_line(data_iter)
persons_iter = get_persons_older_25(data)
# print(*persons_iter)
print(f'Persons older 25 are: {", ".join(persons_iter)}')
