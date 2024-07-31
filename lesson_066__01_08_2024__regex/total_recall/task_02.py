"""Реализуйте класс библиотеки Library,
с атрибутом
    - shelf: список, представляющий полку библиотеки
и методом
    - add_book: добавляет новую книгу на полку библиотеки,
                используя метод Book.create_book()..

Также необходимо создать (переопределить) некоторые dunder методы (см.примеры вывода)
"""


from task_01 import Book


class Library:
    pass


library = Library()

library.add_book("War and Peace", "Leo Tolstoy")
library.add_book("Pride and Prejudice", "Jane Austen")
library.add_book("Ten Little Niggers", "Agatha Christie")
library.add_book("Gone with the Wind", "Margaret Mitchell")


print(library[:2])
# ['Book War and Peace by Leo Tolstoy', 'Book Pride and Prejudice by Jane Austen']

print(library[0])
# Book War and Peace by Leo Tolstoy

print(library)
# The total number of books in the library is 4:
#  - Book "War and Peace" by Leo Tolstoy
#  - Book "Pride and Prejudice" by Jane Austen
#  - Book "Ten Little Niggers" by Agatha Christie
#  - Book "Gone with the Wind" by Margaret Mitchell
