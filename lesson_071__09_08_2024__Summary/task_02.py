"""Найдите и выведите на печать содержимое всех селекторов “class” в
html-кода на указанной веб-странице.
При решении задачи необходимо использовать библиотеку bs4.
"""


import requests
from bs4 import BeautifulSoup


def get_all_selectors_class(url):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all(class_=True)
        for class_ in set(tags):
            print(class_['class'][0])
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")


url = 'https://ru.wikipedia.org/wiki/Wi-Fi'
get_all_selectors_class(url)

# vector-menu-portal
# interwiki-sq
# mbox-image
# toctogglespan
# interwiki-io
# selflink
# interwiki-da
# interwiki-vi
# noprint
# vector-search-box
