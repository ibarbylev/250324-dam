"""Напишите функцию highlight_keywords(text, keywords),
которая выделяет все вхождения заданных ключевых слов в тексте,
окружая их символами *.
Функция должна быть регистро-независимой при поиске ключевых слов.
"""
import re
from typing import List


def highlight_keywords(text: str, key_words: List[str]) -> str:
    new_text = text
    for k in key_words:
        new_text = re.sub(f"({k})",
                          r'*\1*', new_text,
                          flags=re.IGNORECASE
                          )
    return new_text


text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]

print(highlight_keywords(text, keywords))
# This is a sample text. We need to highlight *Python* and *programming*.
