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

def pars_line(line):
    pass


def read_file(filename):
    pass


def get_the_oldest_person(data: Iterator) -> tuple[str, int]:
    return max(data, key=lambda x: x[1])


def get_persons_older_25(data: Iterator) -> Iterator[str]:
    return (p[0] for p in data if p[1] > 25)


data_iter = read_file('persons.txt')
person_name, _ = get_the_oldest_person(data_iter)
print(f'The oldest man is {person_name}.')

data_iter = read_file('persons.txt')
persons_iter = get_persons_older_25(data_iter)
print(f'Persons older 25 are: {", ".join(persons_iter)}')
