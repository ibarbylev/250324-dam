"""https://beautiful-soup-4.readthedocs.io/en/latest/"""


import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/REST"

response = requests.get(URL)
if response.status_code == 200:

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Извлечение заголовков
    titles = soup.find_all("h2")
    for title in titles:
        print(title)

    # Извлечение текста заголовков
    for title in titles:
        print(title.text)

    # Извлечение текста параграфа
    paragraph = soup.find("p").text
    print('paragraph', paragraph)

    # Извлечение ссылки
    link = soup.find("a")["href"]
    print('linl =', link)


