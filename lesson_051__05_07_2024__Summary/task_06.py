"""Напишите скрипт, который обрабатывает аргументы командной строки.
В аргументах командной строки необходимо передать домен и номер порта в формате:
--domain website.com --port 8888
Необходимо учесть, что допустим и другой вариант:
--port 8888 --domain website.com
В итоге скрипт должен вывести словарь {"url": url, "port": 8889}, где
 - url = 'http://' + domain
 - port = port + 1

Если командная строка содержит честь аргументов (или не содержит совсем),
то вместо отсутствующих данных необходимо вывести значения по умолчанию:
{"url": "http://127.0.0.1", "port": 8000}


python task_06.py --domain website.com --port 8888
"""

import sys

dct = {
    "domain": "http://127.0.0.1",
    "port": 8000
}

try:
    args = sys.argv[1:]
    if args:
        if '--domain' in args:
            idx = args.index('--domain')
            if idx + 1 < len(args):
                dct["domain"] = 'http://' + args[idx + 1]

        if '--port' in args:
            idx = args.index('--port')
            if idx + 1 < len(args):
                dct["port"] = int(args[idx + 1]) + 1

except Exception as e:
    print(f"{e.__class__.__name__}: {e}")

print(dct)

# python task_06.py --domain website.com --port 8888