"""Напишите программу, которая
    - запрашивает у пользователя URL-адрес веб-страницы
    - и уровень заголовков (теги h1, h2, h3 и т.д.),
а затем использует библиотеку Beautiful Soup для парсинга HTML
и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
"""

import requests
from bs4 import BeautifulSoup


def get_headers(url, header_tag):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all(header_tag)
        return headers
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return []


# url = input("Введите URL-адрес веб-страницы: ")
# header_tag = input("Введите уровень заголовка (например, h1, h2, h3): ")

url = "https://en.wikipedia.org/wiki/Main_Page"
header_tag = "h2"
headers = get_headers(url, header_tag)

if headers:
    print(f"Заголовки уровня {header_tag}, найденные на странице:")
    for header in headers:
        print(header.text.strip())
else:
    print("Заголовков не найдено.")
