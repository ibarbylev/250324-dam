"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://www.stroysa.tomsk.ru/catalog/derevyannyy_pogonazh/'
response = requests.get(URL)
print(response.content)

# catalog-item-info

# with open('img1.jpg', 'wb') as f:
#     f.write(response.content)
