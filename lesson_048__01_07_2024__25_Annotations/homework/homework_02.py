"""
a.) Напишите программу, которая будет считывать данные о продуктах из файла
и использовать аннотации типов для аргументов и возвращаемых значений функций.
Создайте текстовый файл "products.txt", в котором каждая строка будет содержать
информацию о продукте в формате "название, цена, количество".

Пример:

Apple, 1.50, 10
Banana, 0.75, 15

b.) В программе определите функцию calculate_total_price, которая будет
 - принимать список продуктов и
 - возвращать общую стоимость.
Продумайте, какая аннотация должна быть у аргумента.

c.) Считайте данные из файла, разделите строки на составляющие и создайте список продуктов.

d.) Вызовите функцию calculate_total_price с этим списком и выведите результат.

"""


def read_products(filename: str) -> list[list[str, float, int]]:
    products = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            name, price, quantity = line.strip().split(', ')
            products.append([name, float(price), int(quantity)])
    return products


def calculate_total_price(products: list[list[str, float, int]]) -> float:
    total_price = sum(price * quantity for _, price, quantity in products)
    return total_price


def main() -> None:
    file_path = 'products.txt'
    products = read_products(file_path)

    total_price = calculate_total_price(products)
    print(f"Total price of all products: {total_price:.2f}")


if __name__ == '__main__':
    main()
