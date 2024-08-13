"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://www.stroysa.tomsk.ru/catalog/derevyannyy_pogonazh/'
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='catalog-item-info')

urls = []

card = cards[0]
first_tag_a = card.find('a', href=True)
print(first_tag_a)
url = f'https://www.stroysa.tomsk.ru{first_tag_a.get('href')}'
print(url)

# catalog-item-info

# with open('img1.jpg', 'wb') as f:
#     f.write(response.content)
