"""Напишите функцию find_common_words(url_list),
которая принимает список URL-адресов и возвращает список
наиболее часто встречающихся слов на веб-страницах.

Для каждого URL-адреса функция должна получить содержимое страницы
с помощью запроса GET и использовать регулярные выражения для извлечения слов.
Затем функция должна подсчитать количество вхождений каждого слова и
вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
"""
import re
from collections import Counter
from pprint import pprint

import requests

URL_LIST = [
    'https://ru.wikipedia.org/wiki/REST',
    'https://ru.wikipedia.org/wiki/DNS',
    'https://ru.wikipedia.org/wiki/API',
]


def find_common_words(url_list):
    all_words = []

    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                text = response.text
                words = re.findall(r'\b[A-Za-z]+\b', text.lower())
                all_words.extend(words)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")

    word_counts = Counter(all_words)
    most_common_words = word_counts.most_common(10)
    return most_common_words


res = find_common_words(URL_LIST)
pprint(res)
