"""Словарь синонимов.
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Написать функцию, которая для заданного слова из словаря, определяет его синоним.

Пример словаря:
    dct = {“Hello”: “Hi”, “Bye”: “Goodbye”, “List”: “Array”}

    get_synonym(“Goodbye”) -> Bye.
    get_synonym(“Plate) -> THe word <Plate> was not found in the dictionary!
"""
synonyms = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}


def get_synonym(synonyms: dict, word: str) -> str:

    return "THe word <Plate> not found in the dictionary!"


print(get_synonym(synonyms, "Goodbye"))  # Bye
print(get_synonym(synonyms, "List"))     # Array
print(get_synonym(synonyms, "Plate"))    # Word <Plate> was not found in the dictionary!
