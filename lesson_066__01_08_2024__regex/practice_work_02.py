"""Напишите функцию validate_password(password),
которая принимает строку с паролем и
проверяет его на соответствие следующим условиям:
    - Длина пароля должна быть не менее 8 символов
    - Пароль должен содержать хотя бы
        -- одну заглавную букву,
        -- одну строчную букву и
        -- одну цифру
Пароль может содержать только следующие специальные символы: !@#$%^&*()
"""

import re


def validate_password(password):
    # Проверка длины пароля
    if len(password) < 8:
        return False, "shorter than 8 characters"

    # Проверка наличия хотя бы одной заглавной буквы
    if not re.search(r'...', password):
        return False, 'no capital letter'

    # Проверка наличия хотя бы одной строчной буквы
    if not re.search(r'...', password):
        return False, 'no lowercase letter'

    # Проверка наличия хотя бы одной цифры
    if not re.search(r'...', password):
        return False, 'no digit'

    # Проверка на наличие недопустимых символов
    # [^...] - знак инверсии того, что указано за ^
    if re.search(r'...', password):
        return False, 'invalid character found'

    return True, "it's all right!"


passwords = [
    "Password123!",
    "password123",
    "PASSWORD123",
    "Pass!",
    "Password!",
    "Password1!\\"
]

for password in passwords:
    true_false, text = validate_password(password)
    print(f"{password:12} - {str(true_false):6} {text}")

# Password123! - True   it's all right!
# password123  - False  no capital letter
# PASSWORD123  - False  no lowercase letter
# Pass!        - False  shorter than 8 characters
# Password!    - False  no digit
# Password1!\  - False  invalid character found
