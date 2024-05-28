"""Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для трёх видов скобок (){}[].
"""


def is_valid_brackets(sequence: str) -> bool:
    stack = []
    for s in sequence:
        if s in "({[":
            stack.append(s)
        elif s == ")":
            if not (stack and stack.pop() == "("):
                return False
        elif s == "}":
            if not (stack and stack.pop() == "{"):
                return False
        elif s == "]":
            if not (stack and stack.pop() == "["):
                return False

    return not stack


print(is_valid_brackets("()") == True)         # True
print(is_valid_brackets("([])") == True)       # True
print(is_valid_brackets("{[()]}") == True)     # True
print(is_valid_brackets("{[(])}") == False)    # True
print(is_valid_brackets("{[}") == False)       # True
print(is_valid_brackets("[({})]") == True)     # True
print(is_valid_brackets("[({})](]") == False)  # True
