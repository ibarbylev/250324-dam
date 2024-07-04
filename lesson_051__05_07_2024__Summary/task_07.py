"""Решите предыдущее задание с помощью пакета argparse"""


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--domain', type=str, default='127.0.0.1', help='Enter domain name')
parser.add_argument('--port', type=int, default=8888, help='Enter port number')
args = parser.parse_args()


dct = {
    'domain': f"http://{args.domain}",
    'port': args.port + 1
}

print(dct)

# python task_07.py --domain website.com --port 8888
