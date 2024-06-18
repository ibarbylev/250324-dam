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


def read_json_file(filename: str) -> dict[str, str]:
    pass
    dct = json.load(file)
    return dct


def which_country(city: str) -> str:
    pass
    return "Not found"


print(which_country("Novgorod"))   # Russia
print(which_country("Turin"))      # Italy
print(which_country("Mumbai"))     # Not found
