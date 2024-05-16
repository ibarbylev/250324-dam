from typing import List, Tuple, Set, Dict, Union


def process_data(data: List[str]) -> Tuple[int, Set[str]]:
    # Обработка данных
    return len(data), set(data)


def get_person_details(person: Dict[str, Union[str, int]]) -> str:
    # Получение информации о человеке
    return f"{person['name']}, {person['age']} years old"


print(process_data(['a', 'b', 'c']))

print(get_person_details({'name': 'Ivan', 'age': 25}))


print(' =============================================================== ')


def process_data_2(data: list[str]) -> tuple[int, set[str]]:
    # Обработка данных
    return len(data), set(data)


def get_person_details_2(person: dict[str, str | int]) -> str:
    # Получение информации о человеке
    return f"{person['name']}, {person['age']} years old"


print(process_data_2(['a', 'b', 'c']))

print(get_person_details_2({'name': 'Ivan', 'age': 25}))
