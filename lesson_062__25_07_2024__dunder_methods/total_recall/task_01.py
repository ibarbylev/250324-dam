"""Создать декоратор, который замеряет время работы функции.
Предусмотреть различное число итераций для сглаживания показателя.

Пример:
@param_decorator(5)
def get_request(url: str):
    return requests.get(url).text

get_request('https://google.com')

pip install requests
(pip3 install requests)

"""
import time
import requests



@param_decorator(5)
def get_request(url):
    requests.get(url)


get_request('https://google.com')

# Iteration 1/5
# Delay is 1.21 seconds
# Iteration 2/5
# Delay is 1.23 seconds
# Iteration 3/5
# Delay is 1.43 seconds
# Iteration 4/5
# Delay is 1.43 seconds
# Iteration 5/5
# Delay is 1.02 seconds
# Average time executing get_request:  1.27 seconds
