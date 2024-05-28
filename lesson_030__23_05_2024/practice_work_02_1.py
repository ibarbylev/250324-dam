"""Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для одного вида скобок ().
"""


def is_valid_parentheses(sequence: str) -> bool:
    stack = []
    for s in sequence:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if not (stack and stack.pop() == "("):
                return False

    return not stack


# Примеры использования
print(is_valid_parentheses("()") == True)      # True
print(is_valid_parentheses("(())") == True)    # True
print(is_valid_parentheses("(()())") == True)  # True
print(is_valid_parentheses("(()") == False)    # True
print(is_valid_parentheses(")(") == False)     # True
print(is_valid_parentheses("())(") == False)   # True
