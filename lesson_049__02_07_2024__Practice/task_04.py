"""Возьмите json файл с предыдущего практикума, с клиентами
(имя, фамилия, дата рождения, номер счета)
и реализуйте генератор, который возвращает строки с информацией о клиентах.
Убедитесь, что после вычитывания всех строк из файла,
файловый ресурс корректно освобождается (использования исключения GeneratorExit и очистку ресурсов).
"""
import json
from typing import Generator, Dict


def gen_clients() -> Generator[Dict[str, str], None, None]:
    try:
        with open("users.json", encoding='utf-8') as f:
            lst = json.load(f)
            for i in lst:
                yield i
    except GeneratorExit as e:
        print(f"GeneratorExit, {e}")
    finally:
        f.close()
        print("close")


gen = gen_clients()
for client in gen:
    print(client)
gen.close()


