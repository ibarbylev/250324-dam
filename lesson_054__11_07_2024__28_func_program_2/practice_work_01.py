"""Сгенерировать все возможные комбинации паролей, состоящие из 4 символов,
так, чтобы среди них была хотя бы:
      - одна большая латинская буква,
      - одна маленькая,
      - одна цифра
(и более никаких иных категорий символов, кроме выше указанных!)

При этом запрещено, чтобы
    - символ повторялся в пароле
    - или две соседние по алфавиту буквы стояли рядом.
Записать полученные пароли в файл.

Результат:
Generated 4557072 valid passwords and saved to file.
"""
import itertools
import json

# POSSIBLE_SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
POSSIBLE_SYMBOLS = 'abAB89'


def has_required_characters(password: str) -> bool:
    """Check if the password has at least one uppercase, one lowercase, and one digit."""
    pass


def has_no_repeated_or_sequential_characters(password: str) -> bool:
    """Check if the password has no repeated or sequential characters."""
    pass


def is_valid_password(password: str) -> bool:
    """Check if the password is valid based on the given rules."""
    return (has_required_characters(password)
            and has_no_repeated_or_sequential_characters(password))


def generate_passwords(characters: str) -> list[str]:
    """Generate all valid passwords."""
    permutations = itertools.permutations(characters, 4)
    # ('a', 'b', 'A', 'B'), ('a', 'b', 'A', '8'), ('a', 'b', 'A', '9'), ...
    permutations = (''.join(p) for p in permutations if is_valid_password(p))
    # 'abAB', 'abA8', 'abA9', 'abBA', ...
    return list(permutations)

def write_passwords_to_file(passwords: list[str], filename="tmp.json"):
    """Write the passwords to a file."""
    pass


if __name__ == "__main__":
    valid_passwords = generate_passwords(POSSIBLE_SYMBOLS)
    print(valid_passwords)
    # write_passwords_to_file(valid_passwords)
    print(f"Generated {len(valid_passwords)} valid passwords and saved to file.")