"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://tortocake.com/'
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img', src=True)
print(*img_tags, sep='\n')

# <img src="/img/instafeed/landing/tort-13.jpg"/>
img_scres = ...