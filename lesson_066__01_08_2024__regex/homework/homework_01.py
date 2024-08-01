"""Напишите функцию extract_emails(text),
которая извлекает все адреса электронной почты из заданного текста
и возвращает их в виде списка.
"""
import re


def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-][a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)


text = """
    Here are some emails:
    john.doe@example.com,
    jane_doe123@example.co.uk,
    another.email@sub.example.com,
    invalid-email@example,
    another-invalid-email@example..com
"""
print(*extract_emails(text), sep='\n')

# john.doe@example.com
# jane_doe123@example.co.uk
# another.email@sub.example.com
