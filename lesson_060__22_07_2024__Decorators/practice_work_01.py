"""Создать декоратор, который замеряет время работы функции.
Предусмотреть различное число итераций для сглаживания показателя.

Пример:
@param_decorator(5)
def get_request(url: str):
    return requests.get(url).text

get_request('https://google.com')
"""
import time
import requests
from requests.exceptions import Timeout, RequestException


def param_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for i in range(times):
                print(f"Iteration {i + 1}/{times}")
                start_time = time.time()
                try:
                    func(*args, **kwargs)
                except (Timeout, RequestException):
                    print(f"Timeout, RequestException errors")
                end_time = time.time()
                total_time += end_time - start_time
            average_time = total_time / times
            print(f"Average time for {func.__name__}: {average_time:.6f} seconds")
        return wrapper
    return decorator


@param_decorator(5)
def get_request(url: str):
    return requests.get(url, timeout=5).text


get_request('https://google.com')

# Iteration 1/5
# Iteration 2/5
# Iteration 3/5
# Iteration 4/5
# Iteration 5/5
# Average time for get_request: 0.767245 seconds
