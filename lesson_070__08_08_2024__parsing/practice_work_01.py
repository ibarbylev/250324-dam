"""Написать программу, которая скачивает страницу с сайта на выбор
с актуальным курсом валют, выделяет курс доллара к евро и выводит его.
Можно пользоваться регулярными выражениями и Beautiful Soup вместе.
"""


import requests
from bs4 import BeautifulSoup

url = "https://www.cbr.ru/currency_base/daily/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'data'})

    currency_rates = []

    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        currency_code = columns[1].text.strip()  # Код валюты
        currency_name = columns[3].text.strip()  # Название валюты
        currency_value = columns[4].text.strip()  # Курс валюты
        currency_rates.append((currency_code, currency_name, currency_value))

    # Выводим полученные курсы валют
    for code, name, value in currency_rates:
        print(f"{code} ({name}): {value}")
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")


# AUD (Австралийский доллар): 56,3087
# AZN (Азербайджанский манат): 50,5614
# AMD (Армянских драмов): 22,1686
# BYN (Белорусский рубль): 27,7209
# BGN (Болгарский лев): 47,9690
# BRL (Бразильский реал): 15,2064
# HUF (Венгерских форинтов): 23,5530
# KRW (Вон Республики Корея): 62,6398
# VND (Вьетнамских донгов): 35,4451
# HKD (Гонконгский доллар): 11,0439
# GEL (Грузинский лари): 31,8231
# DKK (Датская крона): 12,5716
# AED (Дирхам ОАЭ): 23,4048
# USD (Доллар США): 85,9543
# EUR (Евро): 93,8419
