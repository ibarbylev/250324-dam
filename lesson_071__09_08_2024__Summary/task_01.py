"""Объясните, что происходит в этом фрагменте кода:"""
from pprint import pprint

import requests

post_params = {'user': 'admin', 'password': 'admin_pass1'}
response = requests.post('https://httpbin.org/post', data=post_params)
pprint(response.json())
# {'args': {},
#  'data': '',
#  'files': {},
#  'form': {'password': 'admin_pass1', 'user': 'admin'},
#  'headers': {'Accept': '*/*',
#              'Accept-Encoding': 'gzip, deflate',
#              'Content-Length': '31',
#              'Content-Type': 'application/x-www-form-urlencoded',
#              'Host': 'httpbin.org',
#              'User-Agent': 'python-requests/2.31.0',
#              'X-Amzn-Trace-Id': 'Root=1-66918acd-5690fb3b5fa770077e869a79'},
#  'json': None,
#  'origin': '188.126.9.72',
#  'url': 'https://httpbin.org/post'}

print(response.json()['form'])
# {'password': 'admin_pass1', 'user': 'admin'}
