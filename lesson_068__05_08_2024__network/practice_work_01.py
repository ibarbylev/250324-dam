"""Написать программу, которая с помощью библиотеки requests
будет проверять доступность сайта, адрес которого передан в аргументе.

Если сайт доступен, необходимо вывести сообщение:
"The site URL is available"
Если нет:
"The site URL is NOT available"

"""

import requests


URL = "https://ru.wikipedia.org/wiki/REST"

response = requests.get(URL)
if response.status_code == 200:
    print(f"The site {URL} is available")
else:
    print(f"The site {URL} is NOT available")


# The site https://ru.wikipedia.org/wiki/REST is available
# The site https://ru.wikipedia.org/wiki/REST/asdfsadfasdf is NOT available