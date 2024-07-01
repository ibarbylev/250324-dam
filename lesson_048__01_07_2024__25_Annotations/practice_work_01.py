"""Реализуйте функцию word_multiply(). Она должна принимать два параметра:

Строку
Число, которое обозначает, сколько раз нужно повторить строку

text = 'python'
print(word_multiply(text, 2)) # => pythonpython
print(word_multiply(text, 0)) # =>

Укажите аннотации типов при объявлении функции.
"""


def word_multiply(word: str, times: int) -> str:
    return word * times


text = 'python'
print(word_multiply(text, 2)) # => pythonpython
print(word_multiply(text, 0)) # =>
