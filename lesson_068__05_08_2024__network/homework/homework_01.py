"""Напишите функцию get_response(url), которая
отправляет GET-запрос по заданному URL-адресу
и возвращает объект ответа.

Затем выведите следующую информацию об ответе:
- Код состояния (status code)
- Текст ответа (response text)
- Заголовки ответа (response headers)
"""

import requests

def get_response(url):
    response = requests.get(url)
    print(response.status_code)  # Выводит код состояния ответа
    print(50 * '=')
    print(response.text[:500])  # Выводит данные, полученные от сервера (первый 500 символов)
    print(50 * '=')
    print(dict(response.headers))


URL = "https://it4each.com"
get_response(URL)