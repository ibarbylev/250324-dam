"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://tortocake.com/img/instafeed/landing/tort-1.jpg'
response = requests.get(URL)
print(response.content)

with open('img1.jpg', 'wb') as f:
    f.write(response.content)
