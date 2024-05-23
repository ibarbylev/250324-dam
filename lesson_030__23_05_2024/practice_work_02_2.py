"""Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для трёх видов скобок (){}[].
"""


def is_valid_brackets(sequence: str) -> bool:
    stack = []

    for char in sequence:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            last_open = stack.pop()
            if char == ')' and last_open != '(':
                return False
            if char == '}' and last_open != '{':
                return False
            if char == ']' and last_open != '[':
                return False

    return not stack


print(is_valid_brackets("()") == True)  # True
print(is_valid_brackets("([])") == True)  # True
print(is_valid_brackets("{[()]}") == True)  # True
print(is_valid_brackets("{[(])}") == False)  # False
print(is_valid_brackets("{[}") == False)  # False
print(is_valid_brackets("[({})]") == True)  # True
print(is_valid_brackets("[({})](]") == False)  # False
