"""Напишите программу, которая
    - запрашивает у пользователя URL-адрес веб-страницы,
    - использует библиотеку Beautiful Soup для парсинга HTML
    - и выводит список всех ссылок на странице.
"""
from typing import List

import requests
from bs4 import BeautifulSoup


def get_links(url: str) -> List[str]:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [link['href'] for link in soup.find_all('a', href=True)]
        return links

    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return []


# url = input("Введите URL-адрес веб-страницы: ")
url = 'https://ru.wikipedia.org/wiki/Wi-Fi'

links = get_links(url)
print(*links, sep='\n')
