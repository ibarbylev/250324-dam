"""Напишите программу, которая
    - запрашивает у пользователя URL-адрес веб-страницы
    - и уровень заголовков (теги h1, h2, h3 и т.д.),
а затем использует библиотеку Beautiful Soup для парсинга HTML
и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
"""

import requests
from bs4 import BeautifulSoup


def get_headers(url, tag=None) -> None:
    if tag is None:
        tags = [f'h{i}' for i in range(1, 7)]
    else:
        tags = [tag]
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in tags:
            headers = soup.find_all(tag)
            print(f'=============== Headers <{tag}> ================:')
            for header in headers:
                print(f'     {header.text.strip()}')
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")


# url = input("Введите URL-адрес веб-страницы: ")
# header_tag = input("Введите уровень заголовка (например, h1, h2, h3): ")

url = 'https://ru.wikipedia.org/wiki/Wi-Fi'
get_headers(url)

