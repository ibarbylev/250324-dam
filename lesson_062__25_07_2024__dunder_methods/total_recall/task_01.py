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


def param_decorator(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for i in range(param):
                print(f"Iteration {i+1}/{param}")
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                delay = end - start
                print(f"Delay is {delay:.2f} seconds")
                total_time += delay
            average_time = total_time / param
            print(f"Average time executing {func.__name__}:  {average_time:.2f} seconds")
        return wrapper
    return decorator


@param_decorator(5)
def get_request(url):
    return requests.get(url).text


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
