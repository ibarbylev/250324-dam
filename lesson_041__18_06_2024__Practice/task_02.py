"""Дан json-файл 'cities-countries.json', в котором
по ключу <Страна> находится строка с названиями городов, разделённых пробелом.

Напишите функцию, которая:
 - считывает данные из файла;
 - по аргументу ГОРОД возвращает
    - либо название страны
    - либо "not found"



which_country("Novgorod") = Russia
which_country("Mumbai") = Not found

"""
import json
from pprint import pprint


def read_json_file(filename: str) -> dict[str, str]:
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def which_country(city: str) -> str:
    pass
    return "Not found"


pprint(read_json_file('cities-countries.json'))
print(which_country("Novgorod"))   # Russia
print(which_country("Turin"))      # Italy
print(which_country("Mumbai"))     # Not found
