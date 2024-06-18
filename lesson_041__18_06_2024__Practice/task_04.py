"""Дополните условие предыдущей задачи:
Информацию о продажах необходимо вывести в файл 'sales-by-customers.json'
"""
import json
from pprint import pprint


def read_list_from_json_file(filename: str) -> dict[str, str]:
    pass


def write_to_json_file(filename: str, dct: dict[str, dict[str, int]]) -> None:
    pass


def process_sales_data(read_from_file: str, write_to_file: str) -> None:
    pass


process_sales_data('sales.json', 'sales-by-customers.json')
