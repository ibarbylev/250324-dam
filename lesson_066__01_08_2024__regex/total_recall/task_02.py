"""Реализуйте класс библиотеки Library, с атрибутом
    - shelf: список, представляющий полку библиотеки
и методами
    - add_book: добавляет новую книгу на полку библиотеки, используя метод Book.create.

Также необходимо создать (переопределить) некоторые dunder методы (см.примеры вывода)
"""


from task_01 import Book


class Library:
    def __init__(self):
        self.shelf = []

    def add_book(self, title, author):
        new_book = Book.create_book(title, author)
        self.shelf.append(new_book)

    def __getitem__(self, index):
        books = self.shelf[index]
        if isinstance(index, slice):
            return [str(book) for book in books]
        return books

    def __str__(self):
        books = "\n".join([f" - {str(b)}" for b in self.shelf])
        return f"The total number of books in the library is {len(self.shelf)}:\n{books}"


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
