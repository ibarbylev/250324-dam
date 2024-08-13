"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://tortocake.com/'
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img', src=True)

# <img src="/img/instafeed/landing/tort-13.jpg"/>
img_urls = [f'https://tortocake.com{i.get('src')}' for i in img_tags]
img_jpg_urls = [i for i in img_urls if '.jpg' in i]
# "https://tortocake.com/img/instafeed/landing/tort-13.jpg"

for idx, url in enumerate(img_jpg_urls[:5]):
    response = requests.get(url)
    with open(f'img_{idx:03d}.jpg', 'wb') as f:
        f.write(response.content)

