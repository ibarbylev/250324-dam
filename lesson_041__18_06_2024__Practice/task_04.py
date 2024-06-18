"""Дополните условие предыдущей задачи:
Информацию о продажах необходимо вывести в файл 'sales-by-customers.json'
"""
import json
from pprint import pprint
from typing import List, Dict


def read_list_from_json_file(filename: str) -> List[str]:
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_to_json_file(filename: str, dct: dict[str, dict[str, int]]) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dct, file, indent=4, ensure_ascii=False)


def process_sales_data(read_from_file: str, write_to_file: str) -> None:
    initial_data: List = read_list_from_json_file(read_from_file)
    sales = {}

    for line in initial_data:
        customer, product, quantity = line.split('-')
        quantity = int(quantity)
        customer_dict = sales.setdefault(customer, {})   # {'apple': 2, 'banana': 7}
        sales[customer][product] = customer_dict.get(product, 0) + quantity

    write_to_json_file(write_to_file, sales)


process_sales_data('sales.json', 'sales-by-customers.json')
