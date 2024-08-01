"""Написать парсер для:
    - телефонных номеров (обработать как можно больше форматов)
    - для email
"""

import re

# Пример текста, содержащего email-адреса
text = """
    Here are some emails:
    john.doe@example.com,
    jane_doe123@example.co.uk,
    jane-doe123@example.co.uk,
    another.email@sub.example.com,
    invalid-email@example,
    another-invalid-email@example..com
"""

# Регулярное выражение для поиска email-адресов
# negative lookbehind  (?<!  )
email_pattern = ...

# Используем findall для нахождения всех совпадений
emails = re.findall(email_pattern, text)

# Вывод найденных email-адресов
print(*emails, sep='\n')
# john.doe@example.com
# jane_doe123@example.co.uk
# jane-doe123@example.co.uk,
# another.email@sub.example.com
