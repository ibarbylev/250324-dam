"""Сколько уникальных слов находится на этой странице:
https://en.wikipedia.org/wiki/REST
При решении необходимо использовать регулярные выражения.
"""

import re
import requests

URL = "https://en.wikipedia.org/wiki/REST"
# [a-zA-Z]+

response = requests.get(URL)
# uniq_words = 0
if response.status_code == 200:
    html = response.text
    pattern = r'[a-zA-Z]+'
    words: list = re.findall(pattern, html)
    # print(len(words))
    uniq_words = set(words)
    # print(len(uniq_words))
else:
    print("Not available!")

print(f"There are {len(uniq_words)} unique words on the {URL} website.")
#  There are 1702 unique words on the https://en.wikipedia.org/wiki/REST website.
