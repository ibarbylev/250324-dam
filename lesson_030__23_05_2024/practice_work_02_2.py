"""Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для трёх видов скобок (){}[].
"""


def is_valid_brackets(sequence: str) -> bool:
    stack = []

    return not stack


print(is_valid_brackets("()") == True)  # True
print(is_valid_brackets("([])") == True)  # True
print(is_valid_brackets("{[()]}") == True)  # True
print(is_valid_brackets("{[(])}") == False)  # False
print(is_valid_brackets("{[}") == False)  # False
print(is_valid_brackets("[({})]") == True)  # True
print(is_valid_brackets("[({})](]") == False)  # False
