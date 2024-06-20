"""Выполнить сериализацию / десериализацию объекта:
person = {"name": "Евгений", "age": 25}

Убедиться в том, словари до преобразования идентичен словарю после.
"""

from json import dump, load

person_source = {"name": "Евгений", "age": 25}
print(type(person_source))  # dict

# Записываем словарь в файл
with open('data.json', 'w', encoding='utf-8') as file:
    dump(person_source, file, ensure_ascii=False, indent=4)


with open('data.json', encoding='utf-8') as file:
    person_destination = load(file)

print(person_destination)
print(person_source == person_destination)
