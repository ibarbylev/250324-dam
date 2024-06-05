"""Дано слово, состоящее только из строчных латинских букв.
Проверьте с помощью рекурсии, является ли это слово палиндромом.
Выведите YES или NO.

Пример:
    is_palindrome("radar") вернёт Yes
    is_palindrome("abba")) вернёт No
    is_palindrome("yes"))  вернёт No
"""


def is_palindrome(word):
    if len(word) <= 1:
        return 'Yes'
    elif word[0] != word[-1]:
        return 'No'
    else:
        return is_palindrome(word[1:-1])


print(is_palindrome("radar"))  # Yes
print(is_palindrome("abba"))   # Yes
print(is_palindrome("yes"))    # No
