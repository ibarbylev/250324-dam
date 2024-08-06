"""Имеется ресурс, где по дате в формате mm/dd можно получить
информацию о знаменательном событии, которое произошло в этот день.
http://numbersapi.com/mm/dd/date  # mm/dd

Напишите программу, которая:
    - формирует и отправляет запрос с сегодняшней датой
    - выводит на печать ответ сервера
"""


from pprint import pprint

import datetime
import requests

today = datetime.date.today()
month = today.month
day = today.day

url = f"http://numbersapi.com/{month}/{day}/date"

response = requests.get(url)
print(response.text)


# http://numbersapi.com/8/5/date
# August 5th is the day in 2003 that a car bomb explodes in the Indonesian capital
# of Jakarta outside the Marriott Hotel killing 12 and injuring 150.
