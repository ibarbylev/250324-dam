"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://www.stroysa.tomsk.ru/catalog/derevyannyy_pogonazh/'
urls = []

for i in range(1, 1000):
    if i == 1:
        url_page = URL
    else:
        url_page = URL + f'?PAGEN_2={i}'

    print(f'?PAGEN_2={i}')

    response = requests.get(url_page)
    if response.status_code != 200:
        break

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='catalog-item-info')

    for card in cards:
        first_tag_a = card.find('a', href=True)
        url = f'https://www.stroysa.tomsk.ru{first_tag_a.get('href')}'
        urls.append(url)
        print(url)

# catalog-item-info

# with open('img1.jpg', 'wb') as f:
#     f.write(response.content)
