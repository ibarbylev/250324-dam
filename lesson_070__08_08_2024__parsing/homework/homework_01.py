"""Напишите программу, которая
    - запрашивает у пользователя URL-адрес веб-страницы,
    - использует библиотеку Beautiful Soup для парсинга HTML
    - и выводит список всех ссылок на странице.
"""

import requests
from bs4 import BeautifulSoup


def get_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [
            a['href'] for a in soup.find_all('a')
            if a['href'][:4] == 'http'
        ]
        return links
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return []


# url = input("Введите URL-адрес веб-страницы: ")
url = "https://en.wikipedia.org/wiki/Main_Page"
links = get_links(url)
print(*links, sep='\n')
