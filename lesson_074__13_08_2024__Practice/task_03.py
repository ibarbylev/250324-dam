"""https://tortocake.com/"""


import requests
from bs4 import BeautifulSoup

URL = 'https://www.flickr.com/explore/'
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('a', href=True)
href_urls = [i.get('href') for i in img_tags if 'photos' in i.get('href')]

print(*href_urls, sep='\n')