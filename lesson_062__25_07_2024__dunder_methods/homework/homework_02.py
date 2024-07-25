"""Реализовать класс Email, представляющий электронное письмо.
Класс должен поддерживать следующие операции:
    - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
    - Преобразование письма в строку (метод __str__)
    - Получение длины текста письма (метод __len__)
    - Получение хеш-значения письма (метод __hash__)
    - Проверка наличия текста в письме (метод __bool__)
"""
import functools
from datetime import datetime


@functools.total_ordering
class Email:
    def __init__(self, to_, from_, subject, text):
        self.to_ = to_
        self.from_ = from_
        self.subject = subject
        self.text = text
        self.date = datetime.now()

    def __bool__(self):
        return bool(self.text)

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date > other.date
    
    def __hash__(self):
        return hash(str(self))
    
    def __len__(self):
        return len(self.text)

    def __str__(self):
        return f"{self.to_} {self.from_} {self.subject} {self.date}"


em1 = Email('Max', 'me', 'hi', 'Hi, dear friend!')
em2 = Email('me', 'Max', 'hi', 'Hi, dear friend!')
empty = Email('me', 'me', '', '')

print(em1)
print(em2)

print(em1 == em2)
print(em1 != em2)
print(em1 >= em2)
print(em1 > em2)
print(em1 <= em2)
print(em1 < em2)

print('len(em1) =', len(em1))
print('len(empty) =', len(empty))

print('hash(em1) =', hash(em1))

print('bool(em1) =', bool(em1))
print('bool(empty) =', bool(empty))
